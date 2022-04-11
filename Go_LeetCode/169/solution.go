package main

import "fmt"

func majorityElement(nums []int) int {
	map_storage := make(map[int]int)
	max_count := 0
	counter := 0
	for _, v := range nums {
		map_storage[v]++
		if map_storage[v] > max_count {
			max_count = map_storage[v]
			counter = v
		}
	}
	fmt.Println(map_storage)
	return counter
}

func main() {
	fmt.Println(majorityElement([]int{3, 2, 3}))
}
