//
// Created by Fabian Stiewe on 02.01.24.
//

using namespace std;

#include <iostream>
#include <vector>

/**
 * Beats around 20%
 */

class SolutionJumpGame_55 {
public:
    bool canJump(vector<int>& nums) {

        std::vector<bool> visited(nums.size(), false);
        int i = 0, step = nums[0];

        while (i <= step && i < nums.size()) {
            visited[i] = true;
            if (nums[i] > step - i){
                step = nums[i] + i;
            }
            i += 1;
        }

        if (visited[visited.size()-1]) return true;
        return false;

    }
};