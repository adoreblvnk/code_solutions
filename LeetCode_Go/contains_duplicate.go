// Contains Duplicate
// Results:
// Runtime: 86 ms, faster than 80.51% of Go online submissions for Contains Duplicate.
// Memory Usage: 8.5 MB, less than 83.78% of Go online submissions for Contains Duplicate.
// https://leetcode.com/submissions/detail/793732733/

package main

import "fmt"

func containsDuplicate(nums []int) bool {
	uniqueMap := map[int]int{}
	for _, val := range nums {
		if _, ok := uniqueMap[val]; ok {
			return true
		}
		uniqueMap[val]++
	}
	return false
}

func main() {
	nums := []int{1, 2, 3, 5}
	fmt.Println(containsDuplicate(nums))
}
