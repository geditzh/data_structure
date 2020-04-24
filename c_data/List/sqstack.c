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
typedef struct {
    SElemType data[MAXSIZE];
    int top;
}SqStack;

Status Push(SqStack *S, SElemType e) {
    if (S->top == MAXSIZE - 1) {
        return FAIL;
    }
    S->top++;
    S->data[S->top] = e;
    return SUCCESS;
}

Status Pop(SqStack *S, SElemType *e) {
    if (S->top == -1) {
        return FAIL;
    }
    *e = S->data[S->top];
    S->top--;
    return SUCCESS;
}

Status Print(SqStack *S) {
    if (S->top == -1) {
        return FAIL;
    }
    int i = 0;
    for (i; i < S->top + 1; i++) {
        printf("%d\t", S->data[i]);
    }
}

int main(int argc, char *argv[])
{
    SqStack stack;
    int e;
    stack.top = -1;
    Push(&stack, 100);
    Push(&stack, 200);
    Print(&stack);
    Pop(&stack, &e);
    Print(&stack);
}
