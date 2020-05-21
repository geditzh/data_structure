#include <stdio.h>

/* 插入排序 */
void InsertSort(int *nums, int len)
{
    int i, j;
    int temp;
    for (i = 1; i < len; i++) {
        temp = nums[i];
        j = i;
        while (j > 0 && nums[j-1] > temp) {
            nums[j] = nums[j-1];
            j--;
        }
        nums[j] = temp;
    }
}

/* 选择排序 */
void SelectSort(int *nums, int len)
{
    int i, j, x;
    int temp;
    for (i = 0; i < len; i++) {
        x = i;
        for (j = i + 1; j < len; j++) {
            if (nums[j] < nums[x]) {
                x = j;
            }
        }
        if (x != i) {
            temp = nums[i];
            nums[i] = nums[x];
            nums[x] = nums[i];
        }
    }
}

int main()
{
    int nums[6] = {5,8,6,1,3,0};
    int len = sizeof(nums) / sizeof(nums[0]);
    int i;
    for (i = 0; i < len; i++) {
        printf("%d, ", nums[i]);
    }
    putchar('\n');
    SelectSort(nums, len);
    for (i = 0; i < len; i++) {
        printf("%d ", nums[i]);
    }
    return 0;
}
