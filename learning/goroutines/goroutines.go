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
}
