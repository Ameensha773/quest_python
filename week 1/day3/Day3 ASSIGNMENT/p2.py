#find smallest and biggest elements in a list of n numbers

number = int(input('Enter how many numbers to elements '))
number_list = [int(input('Enter the numbers ')) for i in range(number)]
number_list.sort()
print('largest number is', number_list[len(number_list)-1]) 
print('Smallest number is', number_list[0])      