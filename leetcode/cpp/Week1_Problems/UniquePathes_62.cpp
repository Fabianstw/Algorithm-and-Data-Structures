//
// Created by Fabian Stiewe on 04.01.24.
//

using namespace std;

#include <iostream>
#include <vector>

class Solution_UniquePaths_62 {
public:
    int uniquePaths(int m, int n) {

        vector<vector<long>> mat(m, vector<long>(n, 0));
        mat[0][0] = 1;

        for (int i = 0; i<m; i++) {
            for (int j = 0; j<n; j++) {
                if (i == 0 && j == 0) {
                    continue;
                } else if (i == 0 && j > 0) {
                    mat[i][j] = mat[i][j-1];
                } else if (i > 0 && j == 0) {
                    mat[i][j] = mat[i-1][j];
                }
                else {
                    mat[i][j] = mat[i-1][j] + mat[i][j-1];
                }
            }
        }

        return static_cast<int>(mat[m-1][n-1] % static_cast<int>(pow(10, 9) * 2));
    }
};