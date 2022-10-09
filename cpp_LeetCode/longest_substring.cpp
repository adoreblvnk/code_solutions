// Longest Substring Without Repeating Characters
// Results:
// Runtime: 18 ms, faster than 76.28% of C++ online submissions for Longest Substring Without
// Repeating Characters.
// Memory Usage: 8.6 MB, less than 46.45% of C++ online submissions for Longest Substring Without
// Repeating Characters.
// https://leetcode.com/submissions/detail/818672419/

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
    // sliding window.
    // use start as left pointer, increment as necessary.
    // use i as right pointer.
    // use hash_map to store if character exists & character positions.
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 1) return 1;
        int max_len{0}, start{0};
        map<char, int> s_map{};
        for (int i{0}; i < s.size(); i++) {
            if (s_map.count(s[i]) && start <= s_map[s[i]]) {
                start = s_map[s[i]] + 1;
            } else {
                max_len = max(max_len, i - start + 1);
            }
            s_map[s[i]] = i;
        }
        return max_len;
    }
};

int main() {
    cout << Solution().lengthOfLongestSubstring((string) "abcabcb") << endl;
    return 0;
}
