package main

import (
	"fmt"
	"time"
)

// Goroutines
func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

// Channels
// only sending
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// sending and receiving
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

// Workers
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {
	// Direct function call
	f("direct")
	// Goroutine
	go f("goroutine")
	// Another Goroutine with anonymous function to show async execution
	go func(msg string) {
		fmt.Println(msg)
	}("going")
	// Sleep to allow goroutines to finish
	time.Sleep(time.Second)
	fmt.Println("done")

	// Channels
	val := make(chan int)
	go func() {
		num := 1
		num += 3
		val <- num
	}()
	result := <-val
	fmt.Println(result)
	// Directions
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
	// Buffered channels
	messages := make(chan string, 2)
	messages <- "buffered"
	messages <- "channel"
	fmt.Println(<-messages)
	// Select
	c1 := make(chan string)
	c2 := make(chan string)
	go func() {
		time.Sleep(time.Second * 1)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "two"
	}()
	fmt.Println(time.Now())
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
	fmt.Println(time.Now())
	// Timeouts
	c3 := make(chan string, 1)
	go func() {
		time.Sleep(time.Second * 2)
		c3 <- "result"
	}()
	select {
	case res := <-c3:
		fmt.Println(res)
	case <-time.After(time.Second * 1):
		fmt.Println("timeout")
	}
	// Non-blocking channel operations
	nonblocking := make(chan string)
	select {
	case msg := <-nonblocking:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}
	// Closing channels
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	<-done

	_, ok := <-jobs
	fmt.Println("received more jobs:", ok)

	// Worker pools
	const numJobs = 5
	jobs2 := make(chan int, numJobs)
	results2 := make(chan int, numJobs)

	for w := 1; w <= 3; w++ {
		go worker(w, jobs2, results2)
	}

	for j := 1; j <= numJobs; j++ {
		jobs2 <- j
	}
	close(jobs2)

	for a := 1; a <= numJobs; a++ {
		<-results2
	}
}
