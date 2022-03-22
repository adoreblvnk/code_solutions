class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(i) for i in s.split() if i.isdigit()]
        return numbers == sorted(set(numbers))

print(Solution.areNumbersAscending("", "5 5"))