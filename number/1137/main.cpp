
// 1137. N-th Tribonacci Number
// author: Greysuki
// ref:
//
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int tribonacci(int n)
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
            return 1;
        }

        int f0 = 0, f1 = 1, f2 = 1, fi;
        for (int i = 3; i <= n; i++)
        {
            fi = f0 + f1 + f2;

            f0 = f1;
            f1 = f2;
            f2 = fi;
        }

        return fi;
    }
};

int main()
{

    Solution sol = Solution();
    int qst1 = 4;
    auto ans1 = sol.tribonacci(qst1);
    cout << ans1 << endl;

    int qst2 = 25;
    auto ans2 = sol.tribonacci(qst2);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}