#include <iostream>

#include "Week1_Problems/ThreeSum.cpp"
#include "Week1_Problems/PrintWordsVertically_1324.cpp"
#include "Week1_Problems/LongestCommonPrefix_14.cpp"
#include "Week1_Problems/JumpGame_55.cpp"
#include "Week1_Problems/SearchInRotatedSortedArray_33.cpp"
#include "Week1_Problems/MaximumAreaofaPieceofCakeAfterHorizontalandVerticalCuts_1465.cpp"
#include "Week1_Problems/UniquePathes_62.cpp"
#include "Week1_Problems/FindTheStudentThatWillReplaceTheChalk_1894.cpp"
#include "Week1_Problems/PartitionLabels_763.cpp"
#include "Week1_Problems/BestTimeToBuyAndSellStockWithTransactionfee_714.cpp"

int main()
{

    vector<int> values = {1,3,2,8,4,9};
    int fee = 2;

    Solution sol;

    cout << sol.maxProfit(values, fee);

    return 0;

}
