import math
#find square of range using lamba

 
squares3 = list(map(lambda x: ((x**2) + int(math.sqrt(x))), range(10)))
print('Squares3 = ', squares3)
 
input_numbers = list(map(str, input().split("@")))
print(input_numbers)