// Climbing Stairs
// Results:
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Climbing Stairs.
// Memory Usage: 6 MB, less than 57.11% of C++ online submissions for Climbing Stairs.
// https://leetcode.com/submissions/detail/817738401/

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
    // using DP (Dynamic Programming) & bottom up approach.
    // calculate from the last 2 steps, then calculate backwards.
    int climbStairs(int n) {
        int one{1}, two{1};
        for (int i{0}; i < n - 1; i++) {
            int temp = one;
            one += two;
            two = temp;
        }
        return one;
    }
};

int main() {
    cout << Solution().climbStairs(3) << endl;
    return 0;
}