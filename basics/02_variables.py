# change this code
import math


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and math.isclose(myfloat, 10.0):
    print("Float: %.2f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
