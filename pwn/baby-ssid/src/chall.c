#include <stdio.h>
#include <signal.h>
#include <stdlib.h>


char *flag;

void (*signal(int signum, void (*sighandler)(int)))(int);

void emitflag()
{
    puts(flag);
    exit(1);
}

int main()
{
    char buf[32];
    FILE *fp;

    flag = malloc(100);
    fp = fopen("./flag.txt","r");
    fgets(flag,100,fp);
    fclose(fp);
    signal(SIGSEGV, emitflag);
    fgets(buf,32,stdin);
    printf(buf);

  