//
// Created by Fabian Stiewe on 01.01.24.
//

using namespace std;

#include <iostream>
#include <vector>
#include <map>

/*
 * Runtime is okay, but currently not motivated to find a faster option.
 */

class SolutionLongestCommonPrefix_14 {
    public:
        string longestCommonPrefix(vector<string>& strs) {
            string base = strs[0], prefix = "";

            for (int i = 0; i < base.size(); i++) {
                for (auto & str : strs) {
                    if (base[i] != str[i]) {
                        return prefix;
                    }
                }
                prefix += base[i];
            }

            return prefix;

        }

        string longestCommonPrefix_option1(vector<string>& strs) {

            string result;
            // create a map
            map<string, int> m;

            // iterate through the vector
            for (const auto & str : strs) {
                // iterate through the string
                for (int i = 0; i < str.size(); i++) {
                    // insert the string into the map
                    m[str.substr(0, i + 1)]++;
                }
            }

            // iterate through the map
            for (const auto & [key, value] : m) {
                // if the value is equal to the size of the vector
                if (value == strs.size()) {
                    // if the key is longer than the result
                    if (key.size() > result.size()) {
                        // set the result to the key
                        result = key;
                    }
                }
            }

            return result;

        }
};