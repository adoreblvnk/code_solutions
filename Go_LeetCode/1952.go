package main

import (
	"fmt"
	"math"
)

// Results:
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Three Divisors.
// Memory Usage: 1.9 MB, less than 25.64% of Go online submissions for Three Divisors.

func isThree(n int) bool {
	if n == 1 {
		return false
	}
	square_root := int(math.Sqrt(float64(n)))
	if square_root*square_root != n {
		return false
	}
	for i := 2; i*i <= square_root; i++ {
		if square_root%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isThree(4))
}
