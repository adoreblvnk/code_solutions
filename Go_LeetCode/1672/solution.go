package main

import "fmt"

func maximumWealth(accounts [][]int) int {
	richest := 0
	for _, slice := range accounts {
		wealth := 0
		for _, v := range slice {
			wealth += v
		}
		if wealth > richest {
			richest = wealth
		}
	}
	return richest
}

func main() {
	fmt.Print(maximumWealth([][]int{{1, 2, 3}, {3, 2, 1}}))
}
