
// 198. House Robber
// author: Greysuki
// ref:
// https://leetcode.com/problems/house-robber/
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        if (nums.size() == 1)
        {
            return nums[0];
        }
        else if (nums.size() == 2)
        {
            return max(nums[0], nums[1]);
        }

        int f0 = nums[0];
        int f1 = max(nums[0], nums[1]);
        int fn;
        for (auto i = 2; i < nums.size(); i++)
        {
            fn = max(f1, f0 + nums[i]);
            f0 = f1;
            f1 = fn;
        }

        return fn;
    }
};

int main()
{

    Solution sol = Solution();
    vector<int> qst1 = {2, 3, 2, 2, 3, 2};
    auto ans1 = sol.rob(qst1);
    cout << ans1 << endl;

    vector<int> qst2 = {1, 2, 3, 1, 2, 3};
    auto ans2 = sol.rob(qst2);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}
