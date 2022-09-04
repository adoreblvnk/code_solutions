// Two Sum
// Results:
// Runtime: 6 ms, faster than 87.66% of Go online submissions for Two Sum.
// Memory Usage: 4.4 MB, less than 16.50% of Go online submissions for Two Sum.
// https://leetcode.com/submissions/detail/791105067/

package main

import "fmt"

func twoSum(nums []int, target int) []int {
	hashMap := map[int]int{}
	for idx, val := range nums {
		if _, ok := hashMap[target-val]; ok {
			return []int{hashMap[target-val], idx}
		}
		hashMap[val] = idx
	}
	return []int{}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
