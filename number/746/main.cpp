
// 746. Min Cost Climbing Stairs
// author: Greysuki
// ref:
// https://leetcode.com/problems/climbing-stairs/
#include <iostream>
#include <vector>
using namespace std;

// Fn = Fn-1 + Fn-2
class Solution
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        int f1 = cost[0], f2 = cost[1], fi;
        for (int i = 2; i < cost.size(); i++)
        {
            fi = min(f1, f2);
            f1 = f2;
            f2 = fi + cost[i];
        }

        return min(f1, f2);
    }
};

int main()
{

    Solution sol = Solution();
    vector<int> qst1 = {10, 15, 20};
    auto ans1 = sol.minCostClimbingStairs(qst1);
    cout << ans1 << endl;

    vector<int> qst2 = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
    auto ans2 = sol.minCostClimbingStairs(qst2);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}