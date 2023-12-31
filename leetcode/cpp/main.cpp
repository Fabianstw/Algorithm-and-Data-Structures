#include <iostream>

#include "Week1_Problems/ThreeSum.cpp"

int main()
{
    vector<int> passarg = {-1,0,1,2,-1,-4};
    Solution sol;
    vector<vector<int>> result = sol.threeSum(passarg);
    for (int i = 0; i < result.size(); i++) {
        cout << "[";
        for (int j = 0; j < result[i].size(); j++) {
            cout << result[i][j] << ",";
        }
        cout << "]" << endl;
    }
    return 0;
}
