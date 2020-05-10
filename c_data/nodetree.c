#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define SUCCESS 0
#define FAIL 1

typedef char TElemType;
typedef int Status;

typedef struct TNode {
    TElemType data;
    struct TNode *left, *right;
} BitNode, *BitTree;

Status CreateBiTree(BitTree *T)
{
    TElemType num;
    scanf("%c", &num);
    if (num == '#') {
        *T = NULL;
    } else {
        *T = (BitTree)malloc(sizeof(struct TNode));
        (*T)->data = num;
        CreateBiTree(&(*T)->left);
        CreateBiTree(&(*T)->right);
    }
    return SUCCESS;
}

Status PreOrderTraverse(BitTree T)
{
    if (T == NULL) {
        return FAIL;
    }
    printf("%c", T->data);
    PreOrderTraverse(T->left);
    PreOrderTraverse(T->right);
    return SUCCESS;
}

Status InOrderTraverse(BitTree T)
{
    if (T == NULL) {
        return FAIL;
    }
    InOrderTraverse(T->left);
    printf("%c", T->data);
    InOrderTraverse(T->right);
    return SUCCESS;
}

Status PostOrderTreverse(BitTree T)
{
    if (T == NULL) {
        return FAIL;
    }
    PostOrderTreverse(T->left);
    PostOrderTreverse(T->right);
    printf("%d", T->data);
    return SUCCESS;
}

int main()
{
    BitTree root;
    CreateBiTree(&root);
    InOrderTraverse(root);

    return 0;
}
