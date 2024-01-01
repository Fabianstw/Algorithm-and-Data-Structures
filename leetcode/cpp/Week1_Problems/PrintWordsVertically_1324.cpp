//
// Created by Fabian Stiewe on 01.01.24.
//

using namespace std;

#include <iostream>
#include <vector>

/**
 * Works but it could get optimized ...
 */

class SolutionPrintWordsVertically_1324 {
public:
    vector<string> printVertically(string s) {

        vector<string> result, words;
        int left = 0, right = 0, maxLen = 0;

        // split string into words
        while (right < s.length()) {
            if (s[right] == ' ') {
                string neww = s.substr(left, right - left);
                if (neww.length() > maxLen) {
                    maxLen = neww.length();
                }
                words.push_back(neww);
                left = right + 1;
            }
            right++;
        }
        string neww = s.substr(left, right - left);
        if (neww.length() > maxLen) {
            maxLen = neww.length();
        }
        words.push_back(neww);

        for (int j = 0; j < maxLen; j++) {
            string tmp = "";
            for (int i = 0; i < words.size(); i++) {
                if (words[i].length() <= j) {
                    tmp += ' ';
                }
                else {
                    tmp += words[i][j];
                }
            }
            tmp.erase(tmp.find_last_not_of(' ') + 1);
            result.push_back(tmp);
        }

        return result;
    }
};