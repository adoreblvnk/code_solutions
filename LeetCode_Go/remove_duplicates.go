// Remove Duplicates from Sorted Array
// Results:
// Runtime: 5 ms, faster than 95.21% of Go online submissions for Remove Duplicates from Sorted Array.
// Memory Usage: 4.5 MB, less than 38.32% of Go online submissions for Remove Duplicates from Sorted Array.
// https://leetcode.com/submissions/detail/793551958/

package main

import "fmt"

// 2nd pointer, duplicates, is used to calculate index for unique value.
// NOTE: we do not care about items beyond the 1st 'k' elements.
func removeDuplicates(nums []int) int {
	duplicates := 0
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			duplicates++
		} else {
			nums[i+1-duplicates] = nums[i+1]
		}
	}
	return len(nums) - duplicates
}

func main() {
	nums := []int{1, 1, 2}
	fmt.Println(removeDuplicates(nums))
}
