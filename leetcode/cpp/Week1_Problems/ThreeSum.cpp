//
// Created by Fabian Stiewe on 31.12.23.
//

using namespace std;

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

class SolutionThreeSum {

public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> result;
        set<vector<int>> seen;

        // sort nums
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    vector<int> newSet = {nums[i], nums[left], nums[right]};
                    seen.insert(newSet);
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        result.reserve(seen.size());
        for (const auto& tri : seen) {
            result.push_back(tri);
        }

        return result;

    }



};