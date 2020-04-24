#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAXSIZE 50
#define SUCCESS 0
#define FAIL    1
typedef int Status;
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE];
    int length;
}SqList;

/* 得到线性表的元素 */
Status GetElem(SqList L, int i, ElemType *e)
{
    if (L.length == 0 || i < 1 || i > L.length) {
        return FAIL;
    }
    *e = L.data[i-1];
    return SUCCESS;
}

/* 插入元素 */
Status InsertElem(SqList *L, int i, ElemType e)
{
    int k;
    if (L->length == MAXSIZE) {
        return FAIL;
    }
    if (i < 1 || i > L->length) {
        return FAIL;
    }
    if (i <= L->length) {
        for (k = L->length - 1 ; k >= i - 1; k--) {
            L->data[k+1] = L->data[k];
        }
    }
    L->data[i-1] = e;
    L->length++;
    return SUCCESS;
}

/* 删除表中元素 */
Status ListDelete(SqList *L, int i, ElemType *e)
{
    int k;
    if (L->length == 0) {
        return FAIL;
    }
    if (i < 1 || i > L->length) {
        return FAIL;
    }
    *e = L->data[i-1];
    if (i < L->length) {
        for (k = i - 1; k < L->length - 1; k++) {
            L->data[k] = L->data[k+1];
        }
    }
    L->length--;
    return SUCCESS;
}

Status PrintList(SqList L) {
    if (L.length <= 0)
        return FAIL;
    int i;
    for(i = 0; i < L.length; i++) {
        printf("List[%d] = %d\n", i, L.data[i]);
    }
    return SUCCESS;
}

int main(int argc, char* argv[])
{
    SqList list;
    ElemType e;
    list.data[0] = 500;
    list.length = 1;
    InsertElem(&list, 1, 100);
    PrintList(list);

    InsertElem(&list, 1, 300);
    PrintList(list);

    ListDelete(&list, 2, &e);
    PrintList(list);


    return 0;
}
