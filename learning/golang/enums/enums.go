package main

import "fmt"

// Enums
type ServerState int

// Enum values
const (
	StateStopped ServerState = iota
	StateRunning
	StatePaused
)

// Enum names
var stateName = map[ServerState]string{
	StateStopped: "Stopped",
	StateRunning: "Running",
	StatePaused:  "Paused",
}

// String method for ServerState
func (ss ServerState) String() string {
	return stateName[ss]
}

// Main function
func main() {
	var state ServerState
	fmt.Println(state)
	state = StateRunning
	fmt.Println(state)
	fmt.Println(state.String())
	state = transitionState(state)
	fmt.Println(state)
}

func transitionState(state ServerState) ServerState {
	switch state {
	case StateStopped:
		return StateRunning
	case StateRunning:
		return StatePaused
	case StatePaused:
		return StateStopped
	default:
		panic(fmt.Errorf("Unknown state: %s", state))
	}
}
