
// 1470. Shuffle the Array
// author: Greysuki
// ref:
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
public:
    vector<int> shuffle(const vector<int> &nums, int n)
    {
        vector<int> ans(n * 2, 0);
        for (int i = 0; i < 2 * n; i += 2)
        {
            ans[i] = nums[i / 2];
            ans[i + 1] = nums[n + (i / 2)];
        }

        return ans;
    }
};

int main()
{
    Solution sol = Solution();
    vector<int> ans;

    ans = sol.shuffle({2, 5, 1, 3, 4, 7}, 3);
    print_vector(ans);

    ans = sol.shuffle({1, 2, 3, 4, 4, 3, 2, 1}, 4);
    print_vector(ans);

    ans = sol.shuffle({1, 1, 2, 2}, 2);
    print_vector(ans);

    return 0;
}