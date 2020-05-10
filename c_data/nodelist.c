#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAXSIZE 50
#define SUCCESS 0
#define FAIL    1

typedef int ElemType;
typedef int Status;

typedef struct Node
{
    ElemType data;
    struct Node *next;
} Node;

typedef struct Node *LinkList;

/* 获取链表中的元素 */
Status GetElem(LinkList head, int i, ElemType *e)
{
    int j;
    LinkList p;
    p = head;
    j = 1;
    while (p && j < i) {
        p = p->next;
        j++;
    }
    if (p == NULL || j > i) {
        return FAIL;
    }
    *e = p->data;
    return SUCCESS;
}

 /* 插入节点 */
Status ListInsert(LinkList *head, int i, ElemType e)
{
    int j;
    LinkList p, s;
    p = *head;
    j = 1;
    while (p && j < i) {
        p = p->next;
        j++;
    }
    if (p == NULL) {
        return FAIL;
    }
    s = (LinkList)malloc(sizeof(struct Node));
    s->data = e;
    s->next = p->next;
    p->next = s;

    // s = (LinkList)malloc(sizeof(struct Node));
    // s->data = e;
    // s->next = *head;
    // *head = s;
    return SUCCESS;
}

/* 删除节点 */
Status ListDelete(LinkList head, int i, ElemType *e)
{
    int j;
    LinkList p, q;
    p = head;
    j = 1;
    while (p->next && j < i) {
        p = p->next;
        j++;
    }
    if (p->next == NULL) {
        return FAIL;
    }
    q = p->next;
    p->next = q->next;
    *e = q->data;
    free(q);
    return SUCCESS;
}

Status PrintList(LinkList head)
{
    LinkList p;
    p = head;
    if (p == NULL) {
        return FAIL;
    }
    while (p) {
        printf("%d\n", p->data);
        p = p->next;
    }
    printf("\n");
    return SUCCESS;
}

/* 尾部插入数据 */
Status CreateListTail(LinkList *L, int n)
{
    LinkList p, r;
    *L = (LinkList)malloc(sizeof(Node));
    r = *L;
    int i = 0;
    for (i = 0; i < n-1; i++) {
        p = (LinkList)malloc(sizeof(Node));
        p->data = i;
        r->next = p;
        r = p;\
    }
    r->next = NULL;
}

/* 表格删除 */
Status clearList(LinkList *L)
{
    LinkList p;
    while (*L) {
        p = *L;
        *L = (*L)->next;
        free(p);
    }
    *L = NULL;
    return SUCCESS;
}

Status inverseList(LinkList *Head)
{
    LinkList p, q;
    p = NULL;
    while (*Head) {
        q = *Head;
        *Head = q->next;
        q->next = p;
        p = q;
    }
    *Head = p;
}

int main(int argc, char **argv)
{
    LinkList head;
    CreateListTail(&head, 1);
    ElemType e;
    // PrintList(head);
    ListInsert(&head, 1, 100);
    // PrintList(head);
    ListInsert(&head, 1, 200);
    ListInsert(&head, 1, 300);
    PrintList(head);

    inverseList(&head);
    PrintList(head);
    // ListDelete(head, 1, &e);
    // PrintList(head);

    // clearList(&head);
    // PrintList(head);
    return 0;
}
