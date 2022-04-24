package main

import (
	"fmt"
)

func smallerNumbersThanCurrent(nums []int) []int {
	result := make([]int, len(nums))
	for i, num := range nums {
		for _, v := range nums {
			if num > v {
				result[i]++
			}
		}
	}
	return result
}

func main() {
	fmt.Println(smallerNumbersThanCurrent([]int{8, 1, 2, 2, 3}))
}
