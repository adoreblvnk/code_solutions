// Majority Element
// Results:
// Runtime: 20 ms, faster than 79.58% of Go online submissions for Majority Element.
// Memory Usage: 6.2 MB, less than 73.60% of Go online submissions for Majority Element.
// https://leetcode.com/submissions/detail/793728717/

package main

import "fmt"

// map to store occurrence of each element.
func majorityElement(nums []int) int {
	map_storage := map[int]int{}
	var count, majority int
	for _, val := range nums {
		map_storage[val]++
		if map_storage[val] > count {
			count = map_storage[val]
			majority = val
		}
	}
	return majority
}

func main() {
	nums := []int{3, 2, 3}
	fmt.Println(majorityElement(nums))
}
