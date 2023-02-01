
// A. No return Temp
// author: Greysuki
// ref:
// https://leetcode.com/problems/next-permutation/discuss/1909229/Simple-easy-c%2B%2B-solution
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution
{
public:
    void nextPermutation(vector<int> &nums)
    {
        int pivot = -1;
        for (pivot = nums.size() - 2; pivot >= 0; pivot--)
        {
            if (nums[pivot] < nums[pivot + 1])
            {
                // cout << nums[pivot] << "," << nums[pivot + 1];
                break;
            }
        }

        if (pivot < 0)
        {
            reverse(nums.begin(), nums.end());
            return;
        }

        for (auto i = nums.size() - 1; i > pivot; i--)
        {
            if (nums[pivot] < nums[i])
            {
                swap(nums[pivot], nums[i]);
                break;
            }
        }

        reverse(nums.begin() + pivot + 1, nums.end());
    }
};

int main()
{

    Solution sol = Solution();
    vector<int> qst;
    bool ans;

    // qst = vector<int>{3, 2, 1};
    qst = vector<int>{0, 1, 2, 5, 3, 3, 0};
    sol.nextPermutation(qst);
    for (auto &c : qst)
    {
        cout << c << endl;
    }
    cout << endl;
}