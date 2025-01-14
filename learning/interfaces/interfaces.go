package main

import (
	"fmt"
	"math"
)

// The Interface
type geometry interface {
	area() float64
	perim() float64
}

// Our structs
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Here you can see the implementation of the interface for both structs
// So we can just call area() and perim() on any struct that implements the geometry interface
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// This function takes a geometry interface and calls the area() and perim() methods
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

// This function takes a geometry interface and checks if it's a circle
func detectCircle(g geometry) {
	if c, ok := g.(circle); ok {
		fmt.Println("circle with radius", c.radius)
	}
}

// More info on interfaces
// https://research.swtch.com/interfaces
func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}
	fmt.Println("--- Interfaces ---")

	measure(r)
	measure(c)

	detectCircle(r)
	detectCircle(c)
}
