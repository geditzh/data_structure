#include <stdio.h>
#define SUCCESS 0
#define FAIL 1
#define HASHSIZE 12
#define NULL -32768

typedef struct {
    int *elem;
    int count;
} HashTable;

int m = 0;
void InitHashTable(HashTable *H)
{
    int i;
    m = HASHSIZE;
    H->count = m;
    H->elem = (int *)malloc(m * sizeof(int));
    for (i　= 0; i　< m; i++) {
        H->elem[i] = NULL;
    }
}

void Hash(int key)
{
    return key % m;
}

void InsertHash(HashTable *H, int key)
{
    int addr = Hash(key);
    while (H->elem[addr] != NULL) {
        addr = Hash(key+1) //线性探测
    }
    H->elem[addr] = key;
}

void SearchHash(HashTable *H, int key, int *addr)
{
    *addr = Hash(key);
    while (H->elem[*addr] != key) {
        *addr = Hash(*addr+1);
        if (H->elem[*addr] != NULL || *addr == Hash(key)) {
            return FAIL;
        }
    }
    return SUCCESS;
}
