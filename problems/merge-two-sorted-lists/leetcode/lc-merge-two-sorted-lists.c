/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* result = NULL;
    struct ListNode** lastPtrRef = &result;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            *lastPtrRef = list1;
            list1 = list1->next;
        } else {
            *lastPtrRef = list2;
            list2 = list2->next;
        }
        lastPtrRef = &((*lastPtrRef)->next);
    }

    *lastPtrRef = (list1 != NULL) ? list1 : list2;

    return result;
    
}