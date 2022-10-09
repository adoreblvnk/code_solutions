// Maximum Subarray
// Results:
// Runtime: 119 ms, faster than 93.30% of C++ online submissions for Maximum Subarray.
// Memory Usage: 67.8 MB, less than 10.99% of C++ online submissions for Maximum Subarray.
// https://leetcode.com/submissions/detail/818371827/

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using std::cout, std::endl;
using std::max, std::sort;
using std::string, std::vector, std::map;

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
    int maxSubArray(vector<int>& nums) {
        int max_sum{nums[0]}, current{nums[0]};
        for (int i{1}; i < nums.size(); i++) {
            current += nums[i];
            current = (current > nums[i]) ? current : nums[i];
            max_sum = (max_sum > current) ? max_sum : current;
        }
        return max_sum;
    }
};

int main() {
    vector<int> nums{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << Solution().maxSubArray(nums) << endl;
    return 0;
}
