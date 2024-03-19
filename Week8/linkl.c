#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    Node *head;
    Node *tail; // Tail pointer for efficient insertion at the end
    int size;
} LinkedList;

void make_linkedlist(LinkedList *list);
void linkedlist_insert(LinkedList *list, int value);
void linkedlist_remove(LinkedList *list, int value);
void linkedlist_free(LinkedList *list);

int main() {
    LinkedList list;
    make_linkedlist(&list);

    linkedlist_insert(&list, 1);
    linkedlist_insert(&list, 5);
    linkedlist_insert(&list, 3);
    linkedlist_insert(&list, 2);

    linkedlist_remove(&list, 2);

    printf("Size of linked list: %d\n", list.size);

    linkedlist_insert(&list, 5);
    linkedlist_insert(&list, 5);
    
    printf("Size of linked list after adding two 5s : %d\n", list.size);

    linkedlist_remove(&list, 5);
    printf("Size of linked list after remving 5 : %d\n", list.size);
    linkedlist_free(&list);


    return 0;
}

void make_linkedlist(LinkedList *list) {
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}

void linkedlist_insert(LinkedList *list, int value) {
    Node *newNode = malloc(sizeof(Node));
    if (newNode == NULL) {
        exit(EXIT_FAILURE);
    }
    newNode->data = value;
    newNode->next = NULL;

    if (list->head == NULL) {
        list->head = newNode;
        list->tail = newNode;
    } else {
        list->tail->next = newNode;
        list->tail = newNode;
    }

    list->size++;
}

void linkedlist_remove(LinkedList *list, int value) {
    Node *current = list->head;
    Node *prev = NULL;

    while (current != NULL) {
        if (current->data == value) {
            if (prev == NULL) {
                list->head = current->next;
            } else {
                prev->next = current->next;
            }

            if (current == list->tail) {
                list->tail = prev;
            }

            free(current);
            list->size--;

            current = prev ? prev->next : list->head;
        } else {
            prev = current;
            current = current->next;
        }
    }
}

void linkedlist_free(LinkedList *list) {
    Node *current = list->head;

    while (current != NULL) {
        Node *temp = current;
        current = current->next;
        free(temp);
    }

    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}
