#file handling

input1 = input("enter a number : ")
input2 = input("enter a string : ")
try:
    print(input1,input2, sep=' ')
except TypeError as e:
    print("Error",e)