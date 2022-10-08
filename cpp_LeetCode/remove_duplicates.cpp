// Remove Duplicates from Sorted Array
// Results:
// Runtime: 12 ms, faster than 88.94% of C++ online submissions for Remove Duplicates from Sorted Array.
// Memory Usage: 18.4 MB, less than 74.68% of C++ online submissions for Remove Duplicates from Sorted Array.
// https://leetcode.com/submissions/detail/817605216/

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
    // 2nd pointer, duplicates, is used to calculate index for unique value.
    // NOTE: we do not care about items beyond the 1st 'k' elements.
    int removeDuplicates(vector<int>& nums) {
        int duplicates = 0;
        for (int i{0}; i < nums.size()-1; i++) {
            if (nums[i] == nums[i + 1]) {
                duplicates++;
            } else {
                nums[i + 1 - duplicates] = nums[i + 1];
            }
        }
        return nums.size() - duplicates;
    }
};

int main() {
    vector<int> nums{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    cout << Solution().removeDuplicates(nums) << endl;
    return 0;
}
