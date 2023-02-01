
// 509. Fibonacci Number
// author: Greysuki
// ref:
//
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int fib(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        else if (n == 1)
        {
            return 1;
        }

        int f0 = 0, f1 = 1, fi;
        for (int i = 2; i <= n; i++)
        {
            fi = f0 + f1;

            f0 = f1;
            f1 = fi;
        }

        return fi;
    }
};

int main()
{

    Solution sol = Solution();
    int qst1 = 2;
    auto ans1 = sol.fib(qst1);
    cout << ans1 << endl;

    int qst2 = 4;
    auto ans2 = sol.fib(qst2);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}