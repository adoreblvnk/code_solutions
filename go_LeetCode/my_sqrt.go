// Sqrt(x)
// Results:
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Sqrt(x).
// Memory Usage: 2.1 MB, less than 25.19% of Go online submissions for Sqrt(x).
// https://leetcode.com/submissions/detail/793721729/

package main

import (
	"fmt"
)

// Newton's method
func mySqrt(x int) int {
	sqrt := x
	for sqrt*sqrt > x {
		sqrt = (sqrt + x/sqrt) / 2
	}
	return sqrt
}

func main() {
	x := 4
	fmt.Println(mySqrt(x))
}
