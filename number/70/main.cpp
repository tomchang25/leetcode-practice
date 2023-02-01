
// 70. Climbing Stairs
// author: Greysuki
// ref:
//
#include <iostream>
#include <vector>
using namespace std;

// Fn = Fn-1 + Fn-2
// 5 stair can been step from 4+1 stair or 3+2 stair
class Solution
{
public:
    int climbStairs(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        else if (n == 1)
        {
            return 1;
        }
        else if (n == 2)
        {
            return 2;
        }

        int f1 = 1, f2 = 2, fi;
        for (int i = 3; i <= n; i++)
        {
            fi = f1 + f2;
            f1 = f2;
            f2 = fi;
        }

        return fi;
    }
};

int main()
{

    Solution sol = Solution();
    int qst1 = 3;
    auto ans1 = sol.climbStairs(qst1);
    cout << ans1 << endl;

    int qst2 = 25;
    auto ans2 = sol.climbStairs(qst2);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}