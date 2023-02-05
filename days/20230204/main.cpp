
// 567. Permutation in String
// author: Greysuki
// ref:
#include <iostream>
#include <vector>
using namespace std;

class Solution
{

private:
    vector<int> init_map(string s)
    {
        vector<int> s_map = vector<int>(26, 0);
        for (int i = 0; i < s.size(); i++)
        {
            s_map[s[i] - 'a'] += 1;
        }

        return s_map;
    }

    bool compare_map(vector<int> m1, vector<int> m2)
    {
        for (int i = 0; i < 26; i++)
        {
            if (m1[i] != m2[i])
            {
                return false;
            }
        }

        return true;
    }

public:
    bool checkInclusion(string s1, string s2)
    {

        if (s1.size() > s2.size())
        {
            return false;
        }

        vector<int> s1_map = init_map(s1);
        vector<int> s2_map = init_map(s2.substr(0, s1.size()));

        int index = 0;

        while (index < (s2.size() - s1.size()))
        {
            // print_vector(s1_map);
            // print_vector(s2_map);

            if (compare_map(s1_map, s2_map))
            {
                return true;
            }

            s2_map[s2[index] - 'a'] -= 1;
            s2_map[s2[index + s1.size()] - 'a'] += 1;
            index += 1;
        }

        return compare_map(s1_map, s2_map);
    }
};

int main()
{
    Solution sol = Solution();
    bool ans;

    ans = sol.checkInclusion("ab", "eidbaooo");
    cout << ans << endl
         << endl;

    ans = sol.checkInclusion("ab", "eidboaoo");
    cout << ans << endl
         << endl;

    ans = sol.checkInclusion("adc", "dcda");
    cout << ans << endl
         << endl;

    ans = sol.checkInclusion("hello", "ooolleoooleh");
    cout << ans << endl
         << endl;

    ans = sol.checkInclusion("ab", "eidboaoo");
    cout << ans << endl
         << endl;

    return 0;
}