/*
Basic data types and control structures in Go
*/
package main

import (
	"fmt"
	"math"
	"time"
)

// Constants
const TEXT string = "constant"

func main() {
	// Printing

	// Strings
	fmt.Println("hello world")
	fmt.Println("go" + "lang")
	// Variables
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)
	// Boolean
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)

	// Variables

	// Variable declaration
	var a = "initial"
	fmt.Println(a)
	// Multiple variables
	var b, c int = 1, 2
	fmt.Println(b, c)
	// Type inference
	var d = true
	fmt.Println(d)
	// Zero value
	var e int
	fmt.Println(e)
	//Short hand
	f := "apple"
	fmt.Println(f)

	// Constants
	// - Can be character, string, boolean, or numeric values
	// - Cannot be declared using := syntax
	// - Cannot be changed
	// - Should be in uppercase to differentiate from variables
	fmt.Println("-- Constants --")
	fmt.Println(TEXT)
	const N = 500000000
	const M = 3e20 / N
	fmt.Println(M)
	fmt.Println(int64(M))
	fmt.Println(math.Sin(N))

	// Basic For loops
	// - No while loops
	// - No do-while loops
	// - No parentheses around conditions
	fmt.Println("-- For Loops --")
	// Increment inside loop
	il := 10
	for il <= 13 {
		fmt.Println("increment:", il)
		il = il + 1
	}
	// Classic loop
	for j := 7; j <= 9; j++ {
		fmt.Println("classic:", j)
	}
	// Using range (stops at 2)
	for i := range 3 {
		fmt.Println("range:", i)
	}
	// Break out of infinite loops
	for {
		fmt.Println("loop")
		break
	}
	// Continue to next iteration
	for n := range 6 {
		if n%2 == 0 {
			continue
		}
		fmt.Println("continue:", n)
	}

	// If/Else
	fmt.Println("-- If/Else --")
	// Basic if, note the position of else
	// compared to other languages
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}
	// And, Or, Not
	// &&, ||, !
	if 8%2 == 0 || 9%2 == 0 {
		fmt.Println("at least one number is even")
	}
	// Nested if/else with declartion
	// Braces are also optional, but not recommended
	// No ternary support (condition ? true : false)
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}

	// Switch
	fmt.Println("-- Switch --")
	// Basic
	flag := 2
	fmt.Println("Flag detected is")
	switch flag {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	}
	// Can do multiple checks
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("It's the weekend")
	default:
		fmt.Println("It's a weekday")
	}
	// Type switch against functions/interfaces
	// https://golangdocs.com/interfaces-in-golang
	// Bit complex for me for now
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'm a boolean")
		case int:
			fmt.Println("I'm an integer")
		default:
			fmt.Println("Don't know type", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")

	// Arrays
	// - Fixed size
	// - Zero value is nil
	// - Slice is more common
	// - Good for 2d/3d math
	fmt.Println("-- Arrays --")
	// Declaring and interating with an array
	var arr [5]int
	fmt.Println("arr:", arr)
	arr[4] = 100
	fmt.Println("set:", arr)
	fmt.Println("get:", arr[4])
	fmt.Println("len:", len(arr))
	// Multi-dimensional arrays
	var twoD = [2][3]int{{1, 2, 3}, {4, 5, 6}}
	fmt.Println("2d:", twoD)

	// Slices
	// - Can be resized
	// - Just leave out the element count
	// - Can also use make() to create a slice
	// - Use append() to add elements
	// https://go.dev/blog/slices-intro
	fmt.Println("-- Slices --")
	var s []string
	fmt.Println("slice:", s, "nil:", s == nil, "len:", len(s))
	slice := make([]string, 3)
	fmt.Println("make:", slice, "len:", len(slice), "cap:", cap(slice))
	slice[0] = "a"
	slice[1] = "b"
	slice[2] = "c"
	fmt.Println("set:", slice)
	fmt.Println("get:", slice[2])
	fmt.Println("len:", len(slice))
	slice = append(slice, "d")
	slice = append(slice, "e", "f")
	fmt.Println("append:", slice)
	s = slice[2:5]
	fmt.Println("slice:", s)

	// Maps
	// - Key-value pairs
	// - Zero value is returned of value type if key doesnt exist
	fmt.Println("-- Maps --")
	m := make(map[string]int)
	m["k1"] = 7
	m["k2"] = 13
	fmt.Println("map:", m)
	fmt.Println("get:", m["k1"])
	fmt.Println("len:", len(m))
	fmt.Println("nokey:", m["k3"])
	delete(m, "k2")
	fmt.Println("del:", m)
	clear(m)
	fmt.Println("clear:", m)
	_, prs := m["k2"]
	fmt.Println("present:", prs)

	// Range
	// - Used to iterate over elements in a variety of data structures
	// - Can be used to iterate over key-value pairs in maps
	fmt.Println("-- Range --")
	// Range over slice
	nums := []int{2, 3, 4}
	sum := 0
	// _ is used as index is also provided in range
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)
	// Using index
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}
	// Range over map
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}
	for k := range kvs {
		fmt.Println("key:", k)
	}
	// Range over characters in a string
	// This goes over the unicode code points
	// And something called runes? (i'll look into this later)
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
