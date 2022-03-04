#include <iostream>
#include <memory>
#include <cstdio>
#include <cstring>
#include <unistd.h>

using namespace std;

class Linux {
    public:
    char segments[16];
    long* processIds;

    ~Linux()
    {
        delete [] processIds;
    }


};

unsigned long pad;
unsigned long size;
unsigned long systemAddress;
int AdminCode;

void f()
{
	Linux pc;
    cout<<"Initiating PC Setup.............\n";
    int pid;
	pc.processIds = new long[10];
    cout<<"Enter a base process id to run os : ";
    cin>>pid;
    cout<<"Enter RAM to be allocated : ";
	cin>>size;
	*(long *)&pc.segments[pid] = (long)&systemAddress;
}

int main()
{
    setbuf(stdout, 0);
	setbuf(stdin, 0);
	setbuf(stderr, 0);
	char *p;
	f();
	p = new char[30];
	char z[13];
    cin>>z;
    strncpy(p,z,sizeof(z));
	if (AdminCode == 0xcafebabe) {
		system("/bin/sh");
	}
	exit(0);
}