#program to remove negative numbers in a list

number = int(input('Number of elements: '))
number_list = [int(input('Enter the numbers ')) for i in range(number)]
new_list = []
for i in number_list:
    if(i >= 0):
        new_list.append(i)
    
print(new_list)