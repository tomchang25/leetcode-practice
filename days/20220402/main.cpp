
// 344. Reverse String
// author: Greysuki
// ref:
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
private:
    bool foo(string &s, int l, int r, bool flag = 0)
    {
        if (l >= r)
        {
            return true;
        }

        if (s[l] != s[r])
        {
            if (flag)
            {
                return false;
            }

            return foo(s, l + 1, r, 1) || foo(s, l, r - 1, 1);
        }
        else
        {
            return foo(s, l + 1, r - 1, flag);
        }
    }

public:
    bool validPalindrome(string s)
    {

        return foo(s, 0, s.size() - 1);
    }
};

int main()
{

    Solution sol = Solution();
    string qst;
    bool ans;

    qst = "aba";
    ans = sol.validPalindrome(qst);
    cout << ans << endl;
    cout << endl;

    qst = "abca";
    ans = sol.validPalindrome(qst);
    cout << ans << endl;
    cout << endl;

    qst = "abdcbda";
    ans = sol.validPalindrome(qst);
    cout << ans << endl;
    cout << endl;

    return 0;
}