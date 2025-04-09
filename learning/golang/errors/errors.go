package main

import (
	"errors"
	"fmt"
)

// Basic error handling
func f(arg int) (int, error) {
	if arg == 42 {
		return -1, errors.New("Can't work with 42")
	}
	return arg + 3, nil
}

var ErrOutOfTea = fmt.Errorf("Out of tea")
var ErrPowerFailure = fmt.Errorf("Can't boil water")

func makeTea(arg int) error {
	if arg == 0 {
		return ErrOutOfTea
	}
	if arg == 1 {
		return ErrPowerFailure
	}
	return nil
}

func main() {
	for _, i := range []int{7, 42} {
		if r, e := f(i); e != nil {
			fmt.Println("f failed:", e)
		} else {
			fmt.Println("f worked:", r)
		}
	}

	for _, i := range []int{0, 1, 2} {
		if e := makeTea(i); e != nil {
			fmt.Println("makeTea failed:", e)
		} else {
			fmt.Println("makeTea worked")
		}
	}
}
