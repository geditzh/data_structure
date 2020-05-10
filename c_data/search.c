#include <stdio.h>

/* 暴力搜索的方法 */
int SequetialSearch(int *a, int n, int key)
{
    int i;
    a[0] = key;
    i = n;
    while (a[i] != key) {
        i--;
    }
    return i;
}


/* 二分法查找 */
int BinarySearch(int *a, int len, int key)
{
    int low, high, mid,count;
    count = 0;
    low = 0;
    high = len - 1;
    while (low <= high) {
        count++;
        // mid = low + (high - low) / 2; // 二分法查找
        // mid = low + (high - low) * (key - a[low]) / (a[high] - a[low]); // 插值查找


        if (key < a[mid]) {
            high = mid - 1;
        } else if (key > a[mid]) {
            low = mid + 1;
        } else {
            printf("%d\n", count);
            return mid;
        }
    }
    printf("%d\n", count);
    return -1;
}

int main()
{
    int a[10] = {1,2,3,4,5,6,7,8,9,10};
    int key = 1;
    printf("%d", BinarySearch(a, 10, key));
    return 0;
}
