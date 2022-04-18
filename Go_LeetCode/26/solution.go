package main

import "fmt"

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
	fmt.Println(removeDuplicates([]int{1, 1, 2}))
}
