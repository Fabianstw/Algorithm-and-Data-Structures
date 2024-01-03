//
// Created by Fabian Stiewe on 03.01.24.
//

using namespace std;

#include <iostream>
#include <vector>

/**
 * Beats around 68%
 */

class Solution_SearchInRotatedSortedArray_33 {
public:
    int search(vector<int>& nums, int target) {

        int left = 0, right = nums.size()-1, mid;
        while (left <= right) {
            mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
            }
            else {
                if (nums[right] >= target && target > nums[mid]) {
                    left = mid + 1;
                }
                else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
};