
// 287. Find the Duplicate Number
// author: Greysuki
// ref:
// 1.https://leetcode.com/problems/find-the-duplicate-number/discuss/431491/explaination-about-two-pointers-methodcyclic-sort
// 2.https://leetcode.com/problems/linked-list-cycle-ii/discuss/1701266/C%2B%2B-Explaination-or-Proofs-or-Diagram
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int findDuplicate(vector<int> nums)
    {
        // find meet point
        int slow = nums[0], fast = nums[0];
        do
        {
            slow = nums[slow];
            fast = nums[nums[fast]];

        } while (slow != fast);

        // find entry point
        slow = nums[0];
        while (slow != fast)
        {

            slow = nums[slow];
            fast = nums[fast];
        }

        return slow;
    }
};

int main()
{

    Solution sol = Solution();
    std::vector<int> qst1 = {1, 3, 4, 2, 2};
    auto ans1 = sol.findDuplicate(qst1);
    cout << ans1 << endl;

    std::vector<int> qst2 = {4, 1, 3, 0, 2};
    auto ans2 = sol.findDuplicate(qst2);
    cout << ans2 << endl;

    cout << "Hello world" << endl;

    return 0;
}