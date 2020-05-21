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
            nums[x] = temp;
        }
    }
}

/* 希尔排序 */
void ShellSort(int *nums, int len)
{
    int gap, i, j , temp;
    gap = len / 2;
    while (gap > 0) {
        for (i = gap; i < len; i++) {
            if (nums[i-gap] > nums[i]) {
                temp = nums[i];
                for (j = i-gap; j >= 0 && nums[j] > temp; j -= gap) {
                    nums[j+gap] = nums[j];
                }
                nums[j+gap] = temp;
            }
        }
        gap /= 2;
    }
}

/* 堆排序 */
void siftdown(int *nums, int begin, int end)
{
    int i, j, temp;
    i = begin;
    j = 2 * i + 1;
    temp = nums[i];
    while (j < end) {
        if ((j + 1) < end && nums[j+1] > nums[j]) {
            j = j + 1;
        }
        if (nums[j] < temp) {
            break;
        }
        nums[i] = nums[j];
        i = j;
        j = 2 * j + 1;
    }
    nums[i] = temp;
}

void HeapSort(int *nums, int len)
{
    int i, temp;
    for (i = len / 2; i >= 0; i--) {
        siftdown(nums, i, len);
    }
    for (i = len-1; i >= 0; i--) {
        temp = nums[i];
        nums[i] = nums[0];
        nums[0] = temp;
        siftdown(nums, 0, i);
    }
}

/* 冒泡排序 */
void BubbleSort(int *nums, int len)
{
    int i, j, temp;
    int find;
    for (i = 0; i < len - 1; i++) {
        find = 0;
        for (j = 0; j < len - i - 1; j++) {
            if (nums[j] > nums[j+1]) {
                temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
                find = 1;
            }
        }
        if (find == 0) {
            break;
        }
    }
}

/* 快速排序 */
void QuickSortCore(int * nums, int begin, int end)
{
    int i, j, temp;
    i = begin;
    j = end;
    if (i >= j) {
        return;
    }
    temp = nums[i];
    while (i < j) {
        while ((i < j) && (nums[j] >= temp)) {
            j--;
        }
        if (i < j) {
            nums[i] = nums[j];
            i++;
        }
        while ((i < j) && (nums[i] <= temp)) {
            i++;
        }
        if (i < j) {
            nums[j] = nums[i];
            j--;
        }
    }
    nums[i] = temp;

    QuickSortCore(nums, begin, i-1);
    QuickSortCore(nums, i+1, end);
}
void QuickSort(int *nums, int len)
{
    QuickSortCore(nums, 0, len - 1);
}

/* 归并排序 */
void Merge(int *nums, int start, int mid, int end)
{
    int numsTemp[end-start+1];
    int i, j, o = 0;
    i = start;
    j = mid + 1;
    while (i <= mid && j <= end) {
        if (nums[i] > nums[j]) {
            numsTemp[o++] = nums[j++];
        } else {
            numsTemp[o++] = nums[i++];
        }
    }
    while (i <= mid) {
        numsTemp[o++] = nums[i++];
    }
    while (j <= end) {
        numsTemp[o++] = nums[j++];
    }
    for (o = 0; o < end - start + 1; o++) {
        nums[o + start] = numsTemp[o];
    }
}

void MergeSortDiv(int *nums, int start, int end)
{
    int mid;
    if (start < end) {
        mid = (start + end) / 2;
        MergeSortDiv(nums, start, mid);
        MergeSortDiv(nums, mid+1, end);
        Merge(nums, start, mid, end);
    }
}
void MergeSort(int *nums, int len)
{
    int start, end;
    start = 0;
    end = len - 1;
    MergeSortDiv(nums, start, end);
}

int main()
{
    int nums[9] = {5,8,6,1,3,0,15,4,77};
    int len = sizeof(nums) / sizeof(nums[0]);
    int i;
    for (i = 0; i < len; i++) {
        printf("%d, ", nums[i]);
    }
    putchar('\n');
    MergeSort(nums, len);
    for (i = 0; i < len; i++) {
        printf("%d ", nums[i]);
    }
    getchar();
    return 0;
}
