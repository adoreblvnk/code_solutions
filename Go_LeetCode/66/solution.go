package main

import (
	"fmt"
)

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	new_slice := make([]int, len(digits)+1)
	new_slice[0] = 1
	return new_slice
}

func main() {
	fmt.Println(plusOne([]int{9, 9}))
}
