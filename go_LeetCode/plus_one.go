// Plus One
// Results:
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Plus One.
// Memory Usage: 2 MB, less than 90.35% of Go online submissions for Plus One.
// https://leetcode.com/submissions/detail/793711573/

package main

import "fmt"

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	return append([]int{1}, digits...)
}

func main() {
	digits := []int{9, 9, 9}
	fmt.Println(plusOne(digits))
}
