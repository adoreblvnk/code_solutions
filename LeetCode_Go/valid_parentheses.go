// Valid Parentheses
// Results:
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Valid Parentheses.
// Memory Usage: 2.1 MB, less than 45.81% of Go online submissions for Valid Parentheses.
// https://leetcode.com/submissions/detail/793527191/

package main

import "fmt"

// check top element of stack.
func isValid(s string) bool {
	bracketPair := map[rune]rune{'(': ')', '[': ']', '{': '}'}
	stack := []rune{}
	for _, val := range s {
		switch val {
		case '(', '[', '{':
			stack = append(stack, bracketPair[val])
		default:
			if len(stack) == 0 || stack[len(stack)-1] != val {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}
	return len(stack) == 0
}

func main() {
	s := "]"
	fmt.Println(isValid(s))
}
