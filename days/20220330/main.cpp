
// 74. Search a 2D Matrix
// author: Greysuki
// ref:
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
private:
    int binarySearch(vector<int> &nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else
            {
                return mid;
            }
        }

        return -1;
    }

public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        for (auto row : matrix)
        {
            if (row[row.size() - 1] == target)
            {
                return true;
            }
            else if (row[row.size() - 1] > target)
            {
                return binarySearch(row, target) >= 0;
            }
        }

        return false;
    }
};

int main()
{

    Solution sol = Solution();
    vector<vector<int>> qst1 = {{
        1,
        3,
    }};
    auto ans1 = sol.searchMatrix(qst1, 1);
    cout << ans1 << endl;

    vector<vector<int>> qst2 = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    auto ans2 = sol.searchMatrix(qst2, 13);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}