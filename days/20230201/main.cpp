
// 1071. Greatest Common Divisor of Strings
// author: Greysuki
// ref: https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3024822/greatest-common-divisor-of-strings/
#include <iostream>
using namespace std;

class Solution
{
private:
    int gcd(int _a, int _b)
    {
        int a = max(_a, _b);
        int b = min(_a, _b);

        while (b > 0)
        {
            int t = b;
            b = a % b;
            a = t;
        }

        return a;
    }

public:
    string gcdOfStrings(string str1, string str2)
    {
        size_t str1_len = str1.size();
        size_t str2_len = str2.size();

        if (str1 + str2 != str2 + str1)
        {
            return "";
        }

        return str1.substr(0, gcd(str1_len, str2_len));
    }
};

int main()
{
    Solution sol = Solution();
    string ans;

    ans = sol.gcdOfStrings("ABCABC", "ABC");
    cout << ans << endl
         << endl;

    ans = sol.gcdOfStrings("ABABAB", "ABAB");
    cout << ans << endl
         << endl;

    ans = sol.gcdOfStrings("ABC", "EFG");
    cout << ans << endl
         << endl;

    return 0;
}