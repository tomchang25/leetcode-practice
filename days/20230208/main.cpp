
// 1470. Shuffle the Array
// author: Greysuki
// ref:
#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution
{

private:
public:
    int totalFruit(const vector<int> &fruits)
    {
        map<int, int> baskets;

        int start_index = 0;
        int end_index = 0;

        while (end_index < fruits.size())
        {
            baskets[fruits[end_index]] += 1;

            if (baskets.size() > 2)
            {
                baskets[fruits[start_index]] -= 1;

                if (baskets[fruits[start_index]] == 0)
                {
                    baskets.erase(fruits[start_index]);
                }

                start_index += 1;
            }

            end_index += 1;
        }

        return end_index - start_index;
    }
};

int main()
{
    Solution sol = Solution();
    int ans;

    ans = sol.totalFruit({1, 1, 2, 2, 2, 3, 1, 2});
    cout << ans << endl;

    ans = sol.totalFruit({0, 1, 2, 2});
    cout << ans << endl;

    ans = sol.totalFruit({1, 2, 3, 2, 2});
    cout << ans << endl;

    return 0;
}