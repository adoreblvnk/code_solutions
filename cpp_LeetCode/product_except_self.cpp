// Product of Array Except Self
// Results:
// Runtime: 24 ms, faster than 94.56% of C++ online submissions for Product of Array Except Self.
// Memory Usage: 23.9 MB, less than 87.79% of C++ online submissions for Product of Array Except
// Self. https://leetcode.com/submissions/detail/819140293/

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
    // calculate product of start to i-1 position, & i+1 to end position.
    // initialise vector of size of nums.
    // iterate once to calculate prefix product & set that in i+1 position.
    // iterate twice (backwards) to calculate postfix product & multiply that with i-1 position.
    // •---------•
    // | 1 2 3 4 |
    // •---------•
    // | x 1 2 3 | -> calculate prefix for i+1 position.
    // •---------•
    // | 2 3 4 x | -> calculate postfix for i-1 position (backwards).
    // •---------•
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);
        int pre_product{1}, post_product{1};
        for (int i{0}; i < nums.size() - 1; i++) {
            pre_product *= nums[i];
            result[i + 1] = pre_product;
        }
        for (int i = nums.size() - 1; i > 0; i--) {
            post_product *= nums[i];
            result[i - 1] *= post_product;
        }
        return result;
    }
};

int main() {
    vector<int> nums{1, 2, 3, 4};
    cout << Solution().productExceptSelf(nums) << endl;
    return 0;
}
