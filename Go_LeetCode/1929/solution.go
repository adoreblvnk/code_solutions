package main

import "fmt"

func getConcatenation(nums []int) []int {
	for _, val := range nums {
		nums = append(nums, val)
	}
	return nums
}

func main() {
	fmt.Println(getConcatenation([]int{1, 2, 1}))
}
