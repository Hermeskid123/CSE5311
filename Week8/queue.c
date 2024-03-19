#include <stdio.h>

#define MAX 100

typedef struct {
    int data[MAX];
    int front, rear;
} Queue;

void make_queue(Queue *queue) {
    queue->front = -1;
    queue->rear = -1;
}


void dequeue(Queue *queue, int *value) {
    *value = queue->data[queue->front++];
}
void enqueue(Queue *queue, int value) {
    queue->data[++queue->rear] = value;
    if (queue->front == -1) {
        queue->front = 0;
    }
}


int main() {

    int dequeued = 0;
    Queue queue;
    make_queue(&queue);
    enqueue(&queue, 384);
    enqueue(&queue, 23);
    dequeue(&queue, &dequeued);
    printf("Dequeued: %d\n", dequeued);
    dequeue(&queue, &dequeued);
    printf("Dequeued: %d\n", dequeued);



    return 0;
}

