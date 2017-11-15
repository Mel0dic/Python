#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

int main(int argc, char *argv){

	pthred_t tid;

    printf("Before Thread\n");
    pthread_create(&tid, NULL, myThreadFun, NULL);
    pthread_join(tid, NULL);
    printf("After Thread\n");
    exit(0);

}

void *myThreadFun(void *vargp)
{
    sleep(1);
    printf("Printing GeeksQuiz from Thread \n");
    return NULL;
}