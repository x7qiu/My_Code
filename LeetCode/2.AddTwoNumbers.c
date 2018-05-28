#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy = {0, NULL};
    struct ListNode* current = &dummy;
    int val = 0;
    while (l1 || l2 || val){
        if (l1){
            val += l1->val;
            l1 = l1->next;
        }
        if (l2){
            val += l2->val;
            l2 = l2->next;
        }
        struct ListNode* NewNode = malloc(sizeof(struct ListNode));
        NewNode->val = val%10;
        val = val/10;
        current->next = NewNode;
        current = current->next;
    }
    return dummy.next;
}

int main(){
    
