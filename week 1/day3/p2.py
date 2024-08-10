#Program to check a number is prime or not

number= int(input("Enter a number:  "))
count =0
if(number <=1):
    print('Not prime')
else:
    for i in range(1,number+1):
        if(number%i == 0):
            count+=1
    if(count > 2):
        print(f'{number} is not prime')
    else:
        print(f'{number} is prime')