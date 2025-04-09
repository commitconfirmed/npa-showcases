// Description: This file demonstrates how to create a container struct that contains another struct.
package main

import "fmt"

// base struct
type base struct {
	num int
}

// describe method for base struct
func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// container struct
type container struct {
	base
	str string
}

// describe method for container struct
func main() {

	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	fmt.Println("also num:", co.base.num)

	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	var d describer = co
	fmt.Println("describer:", d.describe())
}
