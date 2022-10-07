// Two Sum
// Results:
// Runtime: 16 ms, faster than 82.57% of C++ online submissions for Two Sum.
// Memory Usage: 11.2 MB, less than 21.04% of C++ online submissions for Two Sum.
// https://leetcode.com/submissions/detail/816896628/

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using std::cout, std::endl, std::string, std::vector, std::map;

// overloads operator << to print formatted vectors.
template <typename T>
std::ostream &operator<<(std::ostream &os, const vector<T> vec) {
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
std::ostream &operator<<(std::ostream &os, const map<T, T1> dict) {
    os << "{";
    if (dict.empty()) {
        return os << "}";
    }
    int i{0};
    for (auto &[key, value] : dict) {
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
    vector<int> twoSum(vector<int> &nums, int target) {
        map<int, int> dict;
        for (int i = 0; i < nums.size(); i++) {
            if (dict.find(target - nums[i]) != dict.end()) {
                return {dict[target - nums[i]], i};
            }
            dict[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    vector<int> nums{2, 7, 11, 15};
    cout << Solution().twoSum(nums, 9) << endl;
    return 0;
}