import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
'''
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("No value at index")
'''