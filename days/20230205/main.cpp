
// 438. Find All Anagrams in a String
// author: Greysuki
// ref: 567. Permutation in String
#include <iostream>
#include <vector>
using namespace std;

template <typename T>
bool print_vector(vector<T> v)
{
    for (auto a : v)
    {
        cout << a << ",";
    }
    cout << endl;
}

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
    vector<int> findAnagrams(string s, string p)
    {
        string s1 = p;
        string s2 = s;
        vector<int> ans = vector<int>();

        if (s1.size() > s2.size())
        {
            return {};
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
                ans.push_back(index);
            }

            s2_map[s2[index] - 'a'] -= 1;
            s2_map[s2[index + s1.size()] - 'a'] += 1;
            index += 1;
        }

        if (compare_map(s1_map, s2_map))
        {
            ans.push_back(index);
        }

        return ans;
    }
};

int main()
{
    Solution sol = Solution();
    vector<int> ans;

    ans = sol.findAnagrams("cbaebabacd", "abc");
    print_vector(ans);

    ans = sol.findAnagrams("abab", "ab");
    print_vector(ans);

    return 0;
}