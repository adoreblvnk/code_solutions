// 3Sum
// Results:
// Runtime: 82 ms, faster than 94.84% of C++ online submissions for 3Sum.
// Memory Usage: 19.9 MB, less than 63.39% of C++ online submissions for 3Sum.
// https://leetcode.com/submissions/detail/817868720/

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
    // 2 pointers.
    // loop through vector, then increase / decrease left / right pointers to fit the remaining sum.
    // NOTE: refer to 2 Sum & 2 Sum II for reference.
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> triplets{};
        std::sort(nums.begin(), nums.end());
        for (int i{0}; i < nums.size(); i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            };
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int three_sum{nums[i] + nums[left] + nums[right]};
                if (three_sum > 0) {
                    right--;
                } else if (three_sum < 0) {
                    left++;
                } else {
                    triplets.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    while (nums[left - 1] == nums[left] && left < right) {
                        left++;
                    }
                }
            }
        }
        return triplets;
    }
};

int main() {
    vector<int> nums{-1, 0, 1, 0};
    cout << Solution().threeSum(nums) << endl;
    return 0;
}