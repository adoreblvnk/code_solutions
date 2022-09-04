package main

import (
	"fmt"
	"sort"
)

func minimumSum(num int) int {
	slice := []int{}
	for num > 0 {
		slice = append(slice, num%10)
		num /= 10
	}
	sort.Ints(slice)
	return (slice[0]+slice[1])*10 + slice[2] + slice[3]
}

func main() {
	fmt.Println(minimumSum(2932))
}
