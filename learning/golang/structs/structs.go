/*
Playing around with functions in Go.
*/
package main

import (
	"fmt"
)

type person struct {
	name string
	age  int
}

func newPerson(name string) *person {
	p := person{name: name}
	p.age = 42
	return &p
}

type rect struct {
	width, height int
}

// Pointer receiver
func (r *rect) area() int {
	return r.width * r.height
}

// Value receiver
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	// Structs
	// - Collection of fields
	// - Fields can be of different types
	// - Fields can be accessed using a dot
	// - Fields can be accessed using a pointer
	// - Mutable
	fmt.Println("-- Structs --")
	fmt.Println(person{"Bob", 20})
	fmt.Println(person{name: "Alice", age: 30})
	fmt.Println(person{name: "Fred"})          // zero indexed
	fmt.Println(&person{name: "Ann", age: 40}) // pointer
	fmt.Println(newPerson("Jon"))
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)
	sp := &s
	fmt.Println(sp.age)
	sp.age = 51
	fmt.Println(sp.age)
	// Methods
	// - Functions with a special receiver argument
	// - Receiver appears in its own argument list between the func keyword and the method name
	r := rect{width: 10, height: 5}
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())
	// Auto conversion between values and pointers
	// Would use this when you don't want to copy the value on each method call
	// Also useful when you want the method to mutate the struct
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}
