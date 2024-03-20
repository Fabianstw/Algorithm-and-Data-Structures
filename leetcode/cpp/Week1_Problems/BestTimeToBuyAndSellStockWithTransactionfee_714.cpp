//
// Created by Fabian Stiewe on 06.01.24.
//

using namespace std;

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

class SolutionBestTimeToBuyAndSellStockWithTransactionFee {

private:
    map<pair<bool, int>, int> memo;

public:

    int maxProfit(vector<int>& prices, int fee) {
        int prev1 = -prices[0], prev2 = 0;

        for (int price : prices) {
            prev1 = max(prev1, prev2 - price);
            prev2 = max(prev2, prev1 + price - fee);
        }

        return prev2;
    }

    int basic_maxProfit(vector<int>& prices, int fee, int curr_value = 0, bool last_buy = false, int round = 0) {

        if (memo.find(make_pair(last_buy, round)) != memo.end()) {
            return curr_value + memo[make_pair(last_buy, round)];
        }

        if (round == prices.size()-1) {
            if (last_buy) {
                return max(curr_value + prices[round], curr_value);
            }
            else {
                return curr_value;
            }
        }

        int max_value;
        if (last_buy) {
            max_value = max(
                    basic_maxProfit(prices, fee,  prices[round], !last_buy, round+1),
                    basic_maxProfit(prices, fee, 0, last_buy, round+1)
                       );
        }
        else {
            max_value = max(
                    basic_maxProfit(prices, fee, - prices[round] - fee, !last_buy, round+1),
                    basic_maxProfit(prices, fee, 0, last_buy, round+1)
            );
        }
        memo[make_pair(last_buy, round)] = max_value;
        return curr_value + max_value;


    }

};