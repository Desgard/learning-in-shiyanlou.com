#include <stdio.h>
#include <string.h>

void sort(char *p[], int n) {
    char *tmp;
    int i, j, k;
    for (i = 0; i < n; ++ i) {
        k = i;
        for (j = i; j < n; ++ j) {
            if (strcmp(p[j], p[k]) < 0) {
                k = j;
            }
        }
        if (k != j) {
            tmp = p[k];
            p[k] = p[i];
            p[i] = tmp;
        }
    }
}

int main() {
    char *courses[] = {"C","C++","PHP","ASP","ASP.NET","C#","JAVA","BASIC","PASCAL","COBOL"};
    int n = 10;
    sort(courses, n);
    int i;
    for (i = 0; i < n; ++ i) {
        printf("%s\n", courses[i]);
    }
    return 0;
}