
// 344. Reverse String
// author: Greysuki
// ref:
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        for (auto i = 0; i < s.size() / 2; i++)
        {
            swap(s[i], s[s.size() - i - 1]);
        }
    }
};

int main()
{

    Solution sol = Solution();
    vector<char> qst1 = {'h', 'e', 'l', 'l', 'o'};
    sol.reverseString(qst1);

    for (auto &c : qst1)
    {
        cout << c << endl;
    }

    cout << endl;

    vector<char> qst2 = {'H', 'a', 'n', 'n', 'a', 'h'};
    sol.reverseString(qst2);
    for (auto &c : qst2)
    {
        cout << c << endl;
    }

    // cout << "Hello world" << endl;

    return 0;
}