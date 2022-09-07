// Richest Customer Wealth
// Results:
// Runtime: 4 ms, faster than 78.67% of Go online submissions for Richest Customer Wealth.
// Memory Usage: 3.1 MB, less than 72.14% of Go online submissions for Richest Customer Wealth.
// https://leetcode.com/submissions/detail/793873754/

package main

import "fmt"

func maximumWealth(accounts [][]int) int {
	var maxWealth int
	for _, val := range accounts {
		var result int
		for _, nestedVal := range val {
			result += nestedVal
		}
		if result > maxWealth {
			maxWealth = result
		}
	}
	return maxWealth
}

func main() {
	accounts := [][]int{{1, 2, 3}, {1, 3, 2}}
	fmt.Println(maximumWealth(accounts))
}
