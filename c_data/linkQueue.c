#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAXSIZE 50
#define SUCCESS 0
#define FAIL    1

typedef int status;
typedef int QElemType;

typedef struct QNode {
    QElemType data;
    struct QNode *next;
} QNode, *QueuePrt;

typedef struct {
    QueuePrt head, rear;
} LinkQueue;

status EnQueue(LinkQueue *Q, QElemType e)
{
    QueuePrt s = (QueuePrt)malloc(sizeof(QNode));
    s->data = e;
    s->next = NULL;
    Q->rear->next = s;
    Q->rear = s;
    return SUCCESS;
}

status DEQueue(LinkQueue Q, QElemtype *e)
{
    QueuePrt p;
    if (Q->head == Q->rear) {
        return FAIL;
    }
    p = Q->head;
    *e = Q->head->data;
    Q->head = Q->head->next;
    free(p);
    return SUCCESS;
}
