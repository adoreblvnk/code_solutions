// Climbing Stairs
// Result:
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Climbing Stairs.
// Memory Usage: 1.9 MB, less than 87.75% of Go online submissions for Climbing Stairs.
// https://leetcode.com/submissions/detail/691632770/

package main

import (
	"fmt"
)

func climbStairs(n int) int {
	a, b := 1, 1
	for n > 0 {
		a, b = b, a+b // fibonacci
		n--
	}
	return a
}

func main() {
	fmt.Println(climbStairs(5))
}
