#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    string minRemoveToMakeValid(string s)
    {
        int c = 0;
        vector<string> st;
        string new_s = "";
        cout << s.length() << endl;
        st.push_back("TTT");
        while (c < s.length())
        {
            cout << new_s << endl;
            cout << s[c] << endl;
            if (s[c] == '(')
            {
                // stack.push_back(c);
            }
            // else if (s[c] == ')')
            // {
            //     if (stack.size() > 0)
            //     {
            //         stack.pop_back();
            //     }
            //     else
            //     {
            //         continue;
            //     }
            // }

            new_s += s[c];
            c += 1;
        }

        return new_s;
    }
};

int main()
{
    Solution sol = Solution();
    auto ret = sol.minRemoveToMakeValid("lee(t(c)o)de)");
    cout << ret << std::endl;
    cout << "Hello world" << endl;

    return 0;
}
