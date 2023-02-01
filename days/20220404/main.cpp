
// A. No return Temp
// author: Greysuki
// ref:
// https://leetcode.com/problems/next-permutation/discuss/1909229/Simple-easy-c%2B%2B-solution
#include <iostream>
#include <vector>
#include <algorithm>
#include "List.h"
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *CreateList(vector<int> arr)
{
    reverse(arr.begin(), arr.end());
    ListNode *next = nullptr;
    ;
    for (auto x : arr)
    {
        ListNode *node = new ListNode(x, next);
        next = node;
    }

    return next;
}

class Solution
{
public:
    ListNode *swapNodes(ListNode *head, int k)
    {
        ListNode *l = head, *r = head;

        for (auto i = 0; i < k - 1; i++)
        {
            l = l->next;
        }

        ListNode *tail = l;
        while (tail->next != nullptr)
        {
            r = r->next;
            tail = tail->next;
        }

        swap(l->val, r->val);

        return head;
    }
};

int main()
{

    Solution sol = Solution();
    ListNode *qst;
    bool ans;

    // qst = vector<int>{3, 2, 1};
    qst = CreateList(vector<int>{1, 2, 3, 4, 5});
    sol.swapNodes(qst, 2);

    do
    {
        cout << qst->val << endl;
        qst = qst->next;
    } while (qst != nullptr);

    return 0;
}