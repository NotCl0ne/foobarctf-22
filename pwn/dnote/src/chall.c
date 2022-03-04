#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

#define MAX_PAGE 20
#define MAX_SIZE 256

typedef unsigned int uint;

char *notes[MAX_PAGE];


void init() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

uint read_int(){
    char buf[16];
    fgets(buf,sizeof(buf),stdin);
    return (uint)atoi(buf);
    }

void create(){
    char *note;
    uint i,size;
    printf("Page no : ");
    i = read_int();
    if( i > MAX_PAGE){
        puts("[!] idx err !!");
        return;
    }
    printf("Name size : ");
    size = read_int();
    if(size > MAX_SIZE){
        puts("[!] size err !!");
    }

    printf("Enter Name : ");
    notes[i] = (char *)malloc(size);
    fgets(notes[i],size,stdin);

}

void show() {
	uint i;

	printf("Page no : ");
	i = read_int();
	if (i > MAX_PAGE) {
		puts("[!] idx err !!");
		return;
	}

	if (notes[i] != NULL) puts(notes[i]);
}

void delete() {
	uint i;

	printf("Page no : ");
	i = read_int();
	if (i > MAX_PAGE) {
		puts("Index out of bounds.");
		return;
	}

	if (notes[i] != NULL) 
        free(notes[i]);
}

void menu() {
	printf(
		"[1] Add Page\n"
		"[2] Show Page\n"
		"[3] Delete Page\n"
		"[4] Quit\n"
		">> "
	);
}

void welcome(){
	puts("╔════════════════════════════════╗");
	puts("║  WELCOME TO VIRTUAL DEADTHNOTE ║");
	puts("╚════════════════════════════════┘");
	puts("\t\t╔═════════╗");
	puts("\t\t║█████████║");
	puts("\t\t║Ð£A†нηΘ†E║");
	puts("\t\t║█████████║");
	puts("\t\t║█████████║");
	puts("\t\t║█████████║");
	puts("\t\t║█████████║");
	puts("\t\t╚═════════┘");
}


int main(void) {
	init();
    welcome();
	while(1) {
		menu();
		switch (read_int()) {
			case 1:
				create();
				break;
			case 2:
				show();
				break;
			case 3:
				delete();
				break;
			case 4:
				exit(0);
			default:
				puts("No such option.");
				break;
		}

	}
	return 0;
}