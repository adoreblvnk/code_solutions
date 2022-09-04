package main

import (
	"fmt"
)

func mySqrt(x int) int {
	for i := 0; i < 100; i++ {
		if i*i > x {
			return i - 1
		}
	}
	return 0
}

func main() {
	fmt.Println(mySqrt(8))
}
