
// 45. Jump Game II

// author: Greysuki
// ref:
#include <iostream>
#include <vector>
using namespace std;

class Solution
{

private:
public:
    int jump(const vector<int> &nums)
    {
        int ans = 0;

        int end_index = 0;
        int jump_index = 0;

        for (int i = 0; i < nums.size() - 1; i++)
        {
            jump_index = max(jump_index, i + nums[i]);

            if (i == end_index)
            {
                ans += 1;
                end_index = jump_index;
            }
        }
        return ans;
    }
};

int main()
{
    Solution sol = Solution();
    int ans;

    ans = sol.jump({2, 5, 1, 1, 1});
    cout << ans << endl;

    ans = sol.jump({2, 3, 1, 1, 4});
    cout << ans << endl;

    ans = sol.jump({2, 3, 0, 1, 4});
    cout << ans << endl;

    return 0;
}