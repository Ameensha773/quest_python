mark = int(input("Enter the mark \n"))
if  (mark >= 0 and mark <=49):
    print("Fail")
elif (mark <= 74):
    print("second class")
elif (mark <= 90):
    print("first class")
elif (mark <= 100):
    print("distinction")
else:
    print("invalid input")