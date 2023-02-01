
// 213. House Robber II
// author: Greysuki
// ref:
// https://leetcode.com/problems/house-robber/
// https://leetcode.com/problems/house-robber-ii/
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
private:
    int rob1(vector<int> &nums, int l, int r)
    {
        if (nums.size() == 1)
        {
            return nums[0];
        }

        int f0 = 0;
        int f1 = nums[l];
        int fn;
        for (auto i = l + 1; i < r; i++)
        {
            fn = max(f1, f0 + nums[i]);
            f0 = f1;
            f1 = fn;
        }

        return f1;
    }

public:
    int rob(vector<int> &nums)
    {
        return max(rob1(nums, 0, nums.size() - 1), rob1(nums, 1, nums.size()));
    }
};

int main()
{

    Solution sol = Solution();
    vector<int> qst1 = {1};
    auto ans1 = sol.rob(qst1);
    cout << ans1 << endl;

    vector<int> qst2 = {1, 2, 3};
    auto ans2 = sol.rob(qst2);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}