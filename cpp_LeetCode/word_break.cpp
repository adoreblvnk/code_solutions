// Word Break

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using std::cout, std::endl;
using std::max, std::min, std::max_element, std::min_element, std::sort, std::reverse;
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
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        // mark true at every index that is able to be segmented.
        for (int i{1}; i <= s.size(); i++) {
            for (int j{0}; j < i; j++) {
                if ((dp[j]) && (find(wordDict.begin(), wordDict.end(), s.substr(j, i - j)) != wordDict.end())) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp.back();
    };
};

int main() {
    string s{"catsandog"};
    vector<string> wordDict{"cats", "dog", "sand", "and", "cat"};
    cout << std::boolalpha << Solution().wordBreak(s, wordDict) << "\n";

    return 0;
}