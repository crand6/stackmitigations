# Nulls suck. Xargs solves issue of program not reading in nulls
# Also, strace lets us see the correct exit code
# Since xargs has own exit code that populates $?
# Also, I'm only interested in last exit() call
python solution.py | xargs --null strace -o tmp_trace ./rop 
tail -n 2 tmp_trace
rm tmp_trace
