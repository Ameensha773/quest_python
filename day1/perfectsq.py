import math
number = int(input("Enter num"))
root = int(math.sqrt(number))
squareroot = root * root
if number == squareroot:
    print("Perfect Square")
else:
    print("not perfect square")