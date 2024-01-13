//
// Created by Fabian Stiewe on 05.01.24.
//

using namespace std;

#include <iostream>
#include <vector>
#include <map>

class Solution_PartitionLabels_763 {
public:
    vector<int> partitionLabels(string s) {

        vector<int> res;
        map<char, int> mapping;

        for (int i = 0; i<s.length(); i++) {
            mapping[s[i]] = i;
        }

        int previ = -1, maxi = 0;
        for (int i = 0; i<s.length(); i++) {
            maxi = max(maxi, mapping[s[i]]);
            if (maxi == i) {
                res.push_back(maxi - previ);
                previ = maxi;
            }
        }

        return res;

    }
};