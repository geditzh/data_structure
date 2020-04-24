#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cpm1(char *s1, char *s2)
{
    int n = strlen(s1);
    int m = strlen(s2);
    int i = 0, j = 0;
    while (i < n && j < m) {
        if (s1[i] == s2[j]) {
            i++;
            j++;
        } else {
            i = i - j + 1;
            j = 0;
        }
    }
    if (j == m) {
        return i - j;
    }
    return -1;
}

int main(int argc, char **argv)
{
    char s1[] = "zhouyishizhu";
    char s2[] = "shizhu"
    printf("%d", cpm1(s1, s2));
}
