// Maximum Product Subarray
// Results:
// Runtime: 3 ms, faster than 98.87% of C++ online submissions for Maximum Product Subarray.
// Memory Usage: 13.9 MB, less than 25.23% of C++ online submissions for Maximum Product Subarray.
// https://leetcode.com/submissions/detail/819052657/

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using std::cout, std::endl;
using std::max, std::min, std::max_element, std::min_element, std::sort;
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
    // store minimum & maximum products to calculate real maximum product.
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        int real_max = *max_element(nums.begin(), nums.end());
        int cur_min{1}, cur_max{1};
        for (auto ele : nums) {
            int temp_max{cur_max};
            cur_max = max({ele * cur_max, ele * cur_min, ele});
            cur_min = min({ele * temp_max, ele * cur_min, ele});
            real_max = max(real_max, cur_max);
        }
        return real_max;
    }
};

int main() {
    vector<int> nums{2, -2, 3, 4};
    cout << Solution().maxProduct(nums) << endl;
    return 0;
}
