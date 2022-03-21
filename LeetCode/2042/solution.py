class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(i) for i in s.split() if i.isdigit()]
        return numbers == sorted(list(set(numbers)))

print(Solution.areNumbersAscending("", "4 5 11 26"))