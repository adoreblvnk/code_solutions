// Median of Two Sorted Arrays
// Results:
// Runtime: 124 ms, faster than 98.86% of C++ online submissions for Best Time to Buy and Sell
// Stock. Memory Usage: 93.4 MB, less than 51.12% of C++ online submissions for Best Time to Buy and
// Sell Stock. https://leetcode.com/submissions/detail/818556402/

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
    // sliding window: move min_price if current price is lower than current min_price.
    int maxProfit(vector<int>& prices) {
        int max_prof{0}, min_price{prices[0]};
        for (auto& ele : prices) {
            if (ele < min_price) {
                min_price = ele;
                continue;
            }
            max_prof = (ele - min_price > max_prof) ? ele - min_price : max_prof;
        }
        return max_prof;
    }
};

int main() {
    vector<int> prices{7, 1, 5, 3, 6, 4};
    cout << Solution().maxProfit(prices) << endl;
    return 0;
}
