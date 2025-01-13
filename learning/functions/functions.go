/*
Playing around with functions in Go.
*/
package main

import (
	"fmt"
)

// Functions
// - Explicit return type
// - Can set the type of concurrent parameters

// Single return
func plusPlus(a, b, c int) int {
	return a + b + c
}

// Multiple return
func vals() (int, int) {
	return 3, 7
}

// Variadic
func variadic(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

// Anonymous functions (closures)
// - Can be used to define functions inside functions
func intSequence() func() int {
	i := 0
	// A function itself is returned
	return func() int {
		i++
		return i
	}
}

// Recursion
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

// Pointers
func zeroval(i_value int) {
	fmt.Println("zeroval(funcbefore):", i_value) // Remove sa0049 error
	i_value = 0
	fmt.Println("zeroval(funcafter):", i_value)
}
func zeroptr(i_pointer *int) {
	*i_pointer = 0
}

func main() {
	// Functions
	fmt.Println("-- Functions --")
	// Single return
	fmt.Println("-- Single --")
	res := plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
	// Multiple return
	fmt.Println("-- Multiple --")
	a, b := vals()
	fmt.Println(a, b)
	// Variadic
	fmt.Println("-- Variadic --")
	variadic(1, 2)
	variadic(1, 2, 3)
	nums := []int{1, 2, 3, 4}
	variadic(nums...) // Splat operator
	// Anonymous functions (closures)
	fmt.Println("-- Anonymous (closures) --")
	nextInt := intSequence()
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	newInts := intSequence()
	fmt.Println(newInts())
	// Recursion
	fmt.Println("-- Recursion --")
	fmt.Println(factorial(7))
	// Pointers
	fmt.Println("-- Pointers --")
	i := 1
	fmt.Println("initial:", i)
	zeroval(i)
	fmt.Println("zeroval:", i)
	zeroptr(&i)
	fmt.Println("zeroptr:", i)
	fmt.Println("pointer:", &i)
}
