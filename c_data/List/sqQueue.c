#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAXSIZE 50
#define SUCCESS 0
#define FAIL    1

typedef int Status;
typedef int QElemType;

typedef struct {
    QElemType data[MAXSIZE];
    int front;
    int rear;
} SqQueue;

Status InitQueue(SqQueue *Q)
{
    Q->front = 0;
    Q->rear = 0;
    return SUCCESS;
}

Status QueueLength(SqQueue Q)
{
    return (Q.rear - Q.front + MAXSIZE) % MAXSIZE;
}

Status EnQueue(Squeue *Q, QElemType e)
{
    if ((Q->rear + 1) % MAXSIZE == Q->front) {
        return FAIL;
    }
    Q->data[Q->rear] = e;
    Q->rear = (Q->rear + 1) % MAXSIZE;
    return SUCCESS;
}

Status DEQueue(SqQueue *Q, QElemType *e)
{
    if (Q->front == Q->reae)
        return FAIL;
    *e = Q->data[Q->front];
    Q->front = (Q->front + 1) % MAXSIZE;
    return SUCCESS;
}
