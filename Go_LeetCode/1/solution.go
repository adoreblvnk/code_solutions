package main

import "fmt"

func twoSum(nums []int, target int) []int {
	hashTable := map[int]int{}
	for i, val := range nums {
		if _, ok := hashTable[target-val]; ok {
			return []int{hashTable[target-val], i}
		}
		hashTable[val] = i
	}
	return []int{}
}

func main() {
	fmt.Println(twoSum([]int{2, 1, 11, 7}, 9))
}
