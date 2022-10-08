// Two Sum II - Input Array Is Sorted
// Results:
// Runtime: 11 ms, faster than 96.55% of C++ online submissions for Two Sum II - Input Array Is
// Sorted.
// Memory Usage: 15.6 MB, less than 43.69% of C++ online submissions for Two Sum II - Input Array Is
// Sorted.
// https://leetcode.com/submissions/detail/817907253/

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using std::cout, std::endl, std::string, std::vector, std::map;

// overloads operator << to print formatted vectors.
template <typename T>
std::ostream& operator<<(std::ostream& os, const vector<T> vec) {
    os << "[";
    if (vec.empty()) {
        return os << "]";
    }
    for (int i{0}; i < vec.size(); i++) {
        os << vec.at(i);
        if (i != vec.size() - 1) {
            os << ", ";
        }
    }
    return os << "]";
}

// overloads operator << to print formatted maps.
template <typename T, typename T1>
std::ostream& operator<<(std::ostream& os, const map<T, T1> dict) {
    os << "{";
    if (dict.empty()) {
        return os << "}";
    }
    int i{0};
    for (auto& [key, value] : dict) {
        os << key << ": " << value;
        if (i < dict.size() - 1) {
            os << ", ";
        }
        i++;
    }
    return os << "}";
}

class Solution {
   public:
    // 2 pointers at left & right of vectors producing a sum.
    // increase / decrease the sum by increasing / decreasing the pointers.
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (left < right) {
            if (numbers[left] + numbers[right] > target) {
                right--;
            } else if (numbers[left] + numbers[right] < target) {
                left++;
            } else {
                return {++left, ++right};
            }
        }
        return {};
    }
};

int main() {
    vector<int> numbers{2, 7, 11, 15};
    cout << Solution().twoSum(numbers, 9) << endl;
    return 0;
}
