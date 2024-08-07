age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female.").lower()
occupation = input("Enter occupation :\n s student \n w working  ").lower()
stay = input('Enter stay location : \n l locality \n h hosteller ').lower()

if gender == 'f':
    if age < 45:
        if occupation == 'w':
            if stay == 'h':
                print("50 rs coupon on nykaa product")
            elif stay == 'l':
                print("50rs coupon on nykaa product")
        elif occupation == 's':
            if stay == 'h':
                print("100rs coupon on nykaa product and discount on book")
            elif stay == 'l':
                print("50% Discount on nykaa product and discount on books")
    elif age >= 45:
        if occupation == 'w':
            if stay == 'h':
                print('25% Discount on all products')
            elif stay == 'l':
                print('25rs Discount on all products')
        elif occupation == 's':
            if stay == 'h':
                print('100rs Discount on all products and books')
            elif stay == 'l':
                print('25% Discount on all products and books')
elif gender == 'm':
    if age < 60:
        if occupation == 'w':
            if stay == 'h':
                print('50% Discount on laptop and phones')
            elif stay == 'l':
                print('40% Discount on laptop and phones')
        elif occupation == 's':
            if stay == 'h':
                print('100rs Discount on titan and fastrack')
            elif stay == 'l':
                print('40% Discount on titan and fasttrack product')
    elif age >= 60:
        if occupation == 'w':
            if stay == 'h':
                print('25% Discount on all products')
            elif stay == 'l':
                print('20% Discount on all products')
        elif occupation == 's':
            if stay == 'h':
                print('25% Discount on all products and books')
            elif stay == 'l':
                print('20% Discount on all products and books')
