
// 1071. Greatest Common Divisor of Strings
// author: Greysuki
// ref: https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3024822/greatest-common-divisor-of-strings/
#include <iostream>
#include <vector>
using namespace std;

class Solution
{

private:
    vector<int> order_map;
    void init_order(string order)
    {
        order_map = vector<int>(order.size(), 0);
        for (int i = 0; i < order.size(); i++)
        {
            order_map[order[i] - 'a'] = i;
        }
    }

    int get_char_order(const char a)
    {
        return order_map[a - 'a'];
    }

public:
    bool isAlienSorted(const vector<string> &words, string order)
    {
        init_order(order);

        vector<string> copy_words = vector<string>(words);

        for (int i = 0; i < copy_words.size(); i++)
        {
            for (int j = 0; j < copy_words[i].size(); j++)
            {
                copy_words[i][j] = get_char_order(copy_words[i][j]) + 'a';
            }
        }

        for (int i = 0; i < copy_words.size() - 1; i++)
        {
            if (copy_words[i].compare(copy_words[i + 1]) > 0)
            {
                return false;
            }
        }

        return true;
    }
};

int main()
{
    Solution sol = Solution();
    bool ans;

    ans = sol.isAlienSorted({"hello", "leetcode"}, "hlabcdefgijkmnopqrstuvwxyz");
    cout << ans << endl
         << endl;

    ans = sol.isAlienSorted({"word", "world", "row"}, "worldabcefghijkmnpqstuvxyz");
    cout << ans << endl
         << endl;

    ans = sol.isAlienSorted({"apple", "app"}, "abcdefghijklmnopqrstuvwxyz");
    cout << ans << endl
         << endl;

    return 0;
}