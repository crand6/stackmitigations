#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
  char buffer[64];
  // Really, libc always linked in with gcc unless --nostdlib
  printf("I'm using printf to include libc\nGive me data\n");
  memcpy(buffer, argv[1], 100);
  return 0;
}
