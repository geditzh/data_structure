#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAXSIZE 50
#define SUCCESS 0
#define FAIL    1

typedef int Status;
typedef int SElemType;

typedef struct StackNode {
    SElemType data;
    struct StackNode *next;
}*LinkStackPtr;

typedef struct LinkStack {
    LinkStackPtr top;
    int count;
}LinkStack;

Status Push(LinkStack *S, SElemType e)
{
    LinkStackPtr s = (LinkStackPtr)malloc(sizeof(struct StackNode));
    s->data = e;
    s->next = S->top;
    S->top = s;
    S->count++;
    return SUCCESS;
}

Status StackEmpty(LinkStack *S)
{
    if (S->count <= 0) {
        return SUCCESS;
    }
    return FAIL;
}


Status Pop(LinkStack *S, SElemType *e)
{
    LinkStackPtr p;
    p = S->top;
    *e = S->top->data;
    S->top = S->top->next;
    free(p);
    S->count--;
    return SUCCESS;
}

Status Print(LinkStack *S)
{
    int i;
    LinkStackPtr p;
    p = S->top;
    for (i = 0; i < S->count; i++) {
        printf("%d\t", p->data);
        p = p->next;
    }
    return SUCCESS;
}

int main(int argc, char**argv)
{
    LinkStack linkstack;
    linkstack.top = NULL;
    linkstack.count = 0;
    Push(&linkstack, 100);
    Push(&linkstack, 200);
    Push(&linkstack, 300);
    SElemType e;
    Pop(&linkstack, &e);
    Print(&linkstack);

}
