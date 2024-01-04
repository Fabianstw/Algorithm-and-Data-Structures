//
// Created by Fabian Stiewe on 04.01.24.
//

using namespace std;

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

/**
 * Beats around 80%
 */

class Solution_MaximumAreaofaPieceofCakeAfterHorizontalandVerticalCuts_1465 {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {

        long res;

        // first sort hori and verti
        horizontalCuts.push_back(h);
        verticalCuts.push_back(w);
        horizontalCuts.push_back(0);
        verticalCuts.push_back(0);
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());

        long hmax = 0, vmax = 0;
        for (int i = 0; i < horizontalCuts.size()-1;i++) {
            if (abs(horizontalCuts[i] - horizontalCuts[i+1]) > hmax) {
                hmax = abs(horizontalCuts[i] - horizontalCuts[i+1]);
            }
        }

        for (int i = 0; i < verticalCuts.size()-1;i++) {
            if (abs(verticalCuts[i] - verticalCuts[i+1]) > vmax) {
                vmax = abs(verticalCuts[i] - verticalCuts[i+1]);
            }
        }

        res = hmax * vmax;

        return static_cast<int>(res % static_cast<int>(pow(10, 9) + 7));

    }
};
