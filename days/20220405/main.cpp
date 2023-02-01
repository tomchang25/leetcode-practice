
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
    int maxArea(vector<int> &height)
    {
        auto l = height.begin(), r = height.end() - 1;

        int width = height.size() - 1;
        int vol = width * min(*r, *l);

        while (l < r)
        {
            if (*l < *r)
            {
                l++;
            }
            else
            {
                r--;
            }

            width--;
            vol = max((width)*min(*r, *l), vol);
        }

        return vol;
    }
};

int main()
{

    Solution sol = Solution();
    vector<int> qst;
    int ans;

    qst = vector<int>{1, 8, 6, 2, 5, 4, 8, 3, 7};
    ans = sol.maxArea(qst);

    cout << ans << endl;

    return 0;
}