#include <stdio.h>

#define SIZE 100

typedef struct {
    int data[SIZE];
    int top;
} Stack;

void make_stack(Stack *stack) {
    stack->top = -1;
}

void stack_push(Stack *stack, int value) {
    stack->data[++stack->top] = value;
}

void stack_pop(Stack *stack, int *value) {
    *value = stack->data[stack->top--];
}

int main() {
    int popped = 0;
    Stack stack;
    make_stack(&stack);
    stack_push(&stack, 5);
    stack_push(&stack, 221);
    
    stack_pop(&stack, &popped);
    
    printf("Popped from stack: %d\n", popped);
    stack_pop(&stack, &popped);
    
    printf("Popped from stack: %d\n", popped);


    return 0;
}

