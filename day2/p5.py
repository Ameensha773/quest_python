# program to find the largest digit in number
number = int(input('Enter a number to find the largest digit: '))

number_list = [int(i) for i in str(number)]

print(f'The largest digit  in {number} is {max(number_list)}')