#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

struct node {
    int             data;
    struct node*    next;
};

// iterate down a LL and compute its length
int length(struct node* head){
    int count = 0;
    struct node* current = head;

    while (current != NULL){
        count++;
        current = current->next;
    }
    return count;
}

// print elements of a LL
void printLL(struct node* head){
    if (head == NULL){
        printf("passed a null pointer!\n");
        return;
    }
    while (head != NULL){
        printf("%d\t", head->data);        
        head = head->next;
    }
    printf("\n");
}

// free the entire LL from memory
void deleteLL(struct node* head){
    struct node* current = head;
    struct node* temp;

    while (current != NULL){
        temp = current;
        current = current->next;
        free(temp);
    }
}

// change a pointer to null
void ChangeToNull(struct node** headRef){
    *headRef = NULL;
}

// add at the front, and update where HEAD points to
// need to call another function to free memory
void Push(struct node** headRef, int data){
    struct node* newNode = malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = *headRef;
    *headRef = newNode;         // this will change the headRef being passed in
}

// Several Ways to build a LL from scrath(in heap), and return the head pointer of it.
// 1) build a LL by adding at the front repeatedly using push() 
// the following example gives back (6,5,4,3,2,1)
struct node* BuildAtHead(){
    struct node* head = NULL;
    int i;
    
    for (i=1; i<6; i++){
        Push(&head, i);
    }

    return head;  // here returning a pointer is OK because memory is managed on *heap* by push 
}

// 2) build by adding at the end
// the following example gives back (1,2,3,4,5,6)
struct node* BuildAtTail(){
    struct node* head = NULL;
    struct node* tail;
    int i;

    // the first node must be added at the head
    Push(&head, 1);
    tail = head;
    // all other nodes can be added at the tail
    for (i=2; i<6; i++){
        Push(&(tail->next), i);
        tail = tail->next;
    }
    return head;
}
// 3) another way to build by adding at the end, using a dummy pointer 
struct node* BuildWithDummy(){
    struct node dummy;
    struct node* tail = &dummy;
    int i;

    dummy.next = NULL;
    for (i=1; i<6; i++){
        Push(&(tail->next), i);
        tail = tail->next;
    }
    return dummy.next;
}

// 4) 
struct node* BuildWithLocalRef(){
    struct node* head = NULL;
    struct node** lastPtrRef = &head;
    int i;

    for (i=1; i<6; i++){
        Push(lastPtrRef, i);
        lastPtrRef = &((*lastPtrRef)->next);
    }
    return head;
}

// Append a node at the end
struct node* AppendNode(struct node** headRef,int num){
    struct node* current = *headRef;
    struct node* newNode = malloc(sizeof(struct node));
    newNode->data = num;
    newNode->next = NULL;

    if (current == NULL){
        *headRef = newNode;
    }
    else{
        while (current->next != NULL){
            current = current->next;
        }
        current->next = NewNode;
    }
}

// Another way to append, using Push()
struct node* AppendWithPush(struct node** headRef, int num){
    struct node* current = *headRef;

    if (current == NULL){
        Push(headRef, num);
    }
    else{
        while (current->next != NULL){
            current = current->next;
        }
        Push(&(current->next), num);
    }
}


void InsertInLinkedList(struct node** head, int data, int position){
    int i = 1;
    struct node* current;
    struct node* prev;
    struct node* newNode = malloc(sizeof(struct node));
    if (!newNode){
        puts("Memory Error");
        return ;
    }
    newNode->data = data;

    current = *head;
    if (position == 1){
        newNode->next = current;
        *head = newNode;
    }
    else {
        while (current && i<position){
            i++;
            prev = current;
            current = current->next;
        }
        if (!current)
            puts("Too deep");
        else {
            newNode->next = current;
            prev->next = newNode;
        }    

    }    
}

void DeleteAtLL(struct node** head, int position){
    int i=1;
    struct node* current;
    struct node* prev;

    current = *head;          
    if (position == 1){
        *head = (*head)->next;
        free(current);
        return;
    }

    while (current && (i<position)){
        prev = current;
        current = current->next;
        i++;
    }

    if (current == NULL){
        puts("no index");
        return;
    }
    else {
        prev->next = current->next;
        free(current);
    }
}


int main(){
    struct node* head = NULL;
    head = BuildAtHead();
    printLL(head);          // 5,4,3,2,1
    deleteLL(head);

    head = BuildAtTail();
    printLL(head);          // 1,2,3,4,5
    deleteLL(head);

    head = BuildWithDummy();
    printLL(head);
    deleteLL(head);

    head = BuildWithLocalRef();
    printLL(head);
    deleteLL(head);
    
/*
    InsertInLinkedList(&head,9, 4); 
    printLL(head);    
    DeleteAtLL(&head, 4);
    printLL(head);
    deleteLL(head);
*/

    return 0;
}
