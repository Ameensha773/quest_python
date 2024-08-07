age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female.")
occupation = input("Enter occupation :\n s student \n w working  ")
stay = input('Enter stay location : \n l locality \n h home ')
parent_job = input("Is your parents in armed force (yes/no): ")

if age >=60 and gender == 'm':
    if occupation == 's':
        print('person cannot get student discount')
    elif occupation =='w':
        if stay == 'h':
            print('Discount on Groceries ')
        else:
            print('15% discount on all products ')
elif age >= 40 and gender == 'f':
    if occupation == 's':
        print('person cannot get student discount')
    elif occupation =='w':
        if stay == 'h':
            print('Discount on Groceries ')
        else:
            print('15% discount on all products ')
elif age < 60 and gender == 'm':
        if occupation == 's':
            if stay == 'h':
                print('Discount on Groceries ')
            else:
                print('500 coupon on books ')
        elif occupation =='w':
            if stay == 'h':
                print('Discount on Groceries ')
            else:
                print('100 rs coupon on titan fast track ')
elif age < 40 and gender == 'f':
    if occupation == 's':
            if stay == 'h':
                print('Discount on Groceries ')
            else:
                print('500 coupon on books')
    elif occupation =='w':
            if stay == 'h':
                print('Discount on Groceries ')
            else:
                print('100 rs coupon on nykaa ')

if parent_job == "yes":
    print("Pass for R-Day parade")
else:
    print("NA")