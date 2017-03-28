#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 重定义数据类型
typedef signed   int    INT32;
typedef signed   char   INT8;


INT32 main(void) {
    INT8  szStrBuf[100] = {0};
    INT8 *pStr          = NULL;

    // 为指针变量分配内存
    pStr = malloc(100);
    if (NULL == pStr)    // 分配失败
    {
        printf("pStr is NULL!\n", pStr);
        return -1;
    }
    memset(pStr, 0x00, 100);

    // 打印初始化变量的值
    printf("Step1: StrBuf=%s, pStr=%s\n", szStrBuf, pStr);

    // 给变量赋值
    memcpy(szStrBuf, "abcdefg", strlen("abcdefg"));
    memcpy(pStr, "1234567", strlen("1234567"));

    // 打印赋值之后的变量的值
    printf("Step2: StrBuf=%s, pStr=%s\n", szStrBuf, pStr);

    // 释放动态内存
    free(pStr);
    pStr = NULL;

    // 打印释放动态内存之后的变量的值
    printf("Step3: StrBuf=%s, pStr=%s\n", szStrBuf, pStr);

    // --------------------

    // 重新为指针变量分配内存
    pStr = malloc(50);
    if (NULL == pStr)    // 分配失败
    {
        printf("pStr is NULL!\n", pStr);
        return -1;
    }
    memset(pStr, 0x00, 50);

    // 给变量赋值
    memcpy(szStrBuf, "abcdefg", strlen("abcdefg"));
    pStr = szStrBuf+1;

    // 打印重新分配动态内存之后的变量的值
    printf("Step4: StrBuf=%s, pStr=%s\n", szStrBuf, pStr);

    // 再次释放动态内存
    free(pStr);
    pStr = NULL;

    // 打印再次释放动态内存之后的变量的值
    printf("Step5: StrBuf=%s, pStr=%s\n", szStrBuf, pStr);

    return 0;
}