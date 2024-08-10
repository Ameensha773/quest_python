#accept N numbers from the user and swap the consecutive elements

number = int(input('Enter numbers to input: '))
number_list = [int(input('Enter the numbers ')) for i in range(number)]
i =0
while i < len(number_list):
    temp = number_list[i]
    number_list[i] = number_list[i+1]
    number_list[i+1] = temp
    i+=2
print('After swapping', number_list)