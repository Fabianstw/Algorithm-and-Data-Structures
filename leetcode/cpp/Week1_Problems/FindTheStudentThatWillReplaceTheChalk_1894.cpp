//
// Created by Fabian Stiewe on 05.01.24.
//

using namespace std;

#include <iostream>
#include <vector>

/**
 * Beats around 80%
 */

class Solution_FindTheStudentThatWillReplaceTheChalk_1894 {
public:
    int chalkReplacer(vector<int>& chalk, int k) {

        long chalk_sum = 0;
        for (int i = 0; i < chalk.size(); i++) {
            if (chalk_sum > k) {
                return i-1;
            }
            chalk_sum += chalk[i];
        }
        k %= chalk_sum;

        for (int i = 0; i < chalk.size(); i++) {
            k -= chalk[i];
            if (k < 0) {
                return i;
            }
        }

        return 0;

    }
};