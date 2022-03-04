#include<stdio.h>

void vuln()
{
    char buffer[64],buffer1[64];
    puts("Can you help find the Canary ?");
    fgets(buffer,sizeof(buffer),stdin);
    printf(buffer);
    fflush(stdout); 
    gets(buffer1);  
    puts(buffer1);
}



int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
}