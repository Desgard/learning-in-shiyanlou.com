#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

void thread() {
    int i;
    for (i = 0; i < 10; ++ i) {
        printf("This is a pthread!\n");
    }
}

int main () {
    pthread_t id;
    int i , ret;
    ret = pthread_create(&id, NULL, (void *)thread, NULL);
    if (ret != 0) {
        printf("Create pthread error!\n");
        exit(1);
    }
    pthread_join(id, NULL);
    for (i = 0; i < 10; ++ i) {
        printf("This is the main process!\n");
    }
    return 0;
}
