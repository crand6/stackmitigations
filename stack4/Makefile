all: no-dep dep
  
no-dep: stack4.c
	gcc -mpreferred-stack-boundary=2 -zexecstack -m32 -fno-inline -fno-stack-protector -std=c99 -O0 -o stack4_nodep stack4.c

dep: stack4.c
	gcc -mpreferred-stack-boundary=2 -m32 -fno-inline -fno-stack-protector -std=c99 -O0 -o stack4_dep stack4.c

clean:
	rm -f stack4_dep stack4_nodep
