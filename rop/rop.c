#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Rop gadget functions
int monkeyMath(int a, int b, int c) {
  int temp = 85;
  temp = a + b - c;
  temp *= 2;
  return temp;
}

int wheelOfRets(int a) {
  int b = 0;
  int c = 1;
  int d = 2;
  int e = 3;
  int f = 5;

  if (a % 3 == 0) {
    printf("A is a multiple of 3\n");
    __asm__("pop %eax; ret;");
  }

  else if (a % 4 == 0 ) {
    printf("I don't do 4's\n");
    exit(5);
  }
  else if (a % 5 == 0) {
    __asm__("int $0x80");
    return 10;
  }

  return a + b + c + d + e;
}

int main(int argc, char **argv) {
  char buffer[64];
  memcpy(buffer, argv[1], 100);
  //gets(buffer);
  //fread(buffer, 1, 100, stdin);
  return 0;
}
