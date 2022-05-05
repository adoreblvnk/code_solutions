package main

import (
	"fmt"
)

// Results:
// Runtime: 26 ms, faster than 85.47% of Go online submissions for Power of Three.
// Memory Usage: 6.2 MB, less than 99.15% of Go online submissions for Power of Three.

func isPowerOfThree(n int) bool {
	return n > 0 && 1162261467%n == 0
}

func main() {
	fmt.Println(isPowerOfThree(27))
}
