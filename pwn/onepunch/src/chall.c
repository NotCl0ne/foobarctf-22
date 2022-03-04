#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>


void init() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int vuln(void){
	char buf[72];
	puts("YOU ONLY GET ONE CHANCE SO....");
	puts("| 👊 Punch harder 👊 |");
	fgets(buf,124,stdin);
	printf(buf);
	return 0;
}


int main(void) {
	init();
	vuln();
	return 0;
}

//gcc chall.c -o chall -Wl,-z,norelro -no-pie