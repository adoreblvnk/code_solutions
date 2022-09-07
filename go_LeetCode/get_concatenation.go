// Concatenation of Array
// Results:
// Runtime: 8 ms, faster than 87.63% of Go online submissions for Concatenation of Array.
// Memory Usage: 6.5 MB, less than 38.76% of Go online submissions for Concatenation of Array.
// https://leetcode.com/submissions/detail/793876408/

package main

import "fmt"

func getConcatenation(nums []int) []int {
	return append(nums, nums...)
}

func main() {
	nums := []int{1, 2, 1}
	fmt.Println(getConcatenation(nums))
}
