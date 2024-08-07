#ecommerce offers including pincode

age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female.").lower()
occupation = input("Enter occupation :\n s student \n w working  ").lower()
stay = input('Enter stay location : \n l locality \n h hosteller ').lower()
discountPin= [100001,100023,100041,100070]

if gender == 'f':
    if age < 45:
        if occupation == 'w':
            if stay == 'h':
                print("100 rs coupon on nykaa product")
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print("50rs coupon on nykaa product")
                else:
                    print('Offer not available in this pincode')    
        elif occupation == 's':
            if stay == 'h':
                print("100rs coupon on nykaa product and discount on book")
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print("50% Discount on nykaa product and discount on books")
                else:
                    print('Offer not available in this pincode')    
    elif age >= 45:
        if occupation == 'w':
            if stay == 'h':
                print('75% Discount on groceries')
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print('75rs Discount on groceries')
                else:
                    print('Offer not available in this pincode')    
        elif occupation == 's':
            if stay == 'h':
                print('100rs Discount on groceries and books')
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print('25% Discount on groceries and books')
                else:
                    print('Offer not available in this pincode')    
elif gender == 'm':
    if age < 60:
        if occupation == 'w':
            if stay == 'h':
                print('50% Discount on laptop and phones')
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print('40% Discount on laptop and phones')
                else:
                    print('Offer not available in this pincode')    
        elif occupation == 's':
            if stay == 'h':
                print('100rs Discount on titan and fastrack')
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print('40% Discount on titan and fasttrack product')
                else:
                    print('Offer not available in this pincode')    
    elif age >= 60:
        if occupation == 'w':
            if stay == 'h':
                print('25% Discount groceries')
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print('20% Discount on groceries')
                else:
                    print('Offer not available in this pincode')    
        elif occupation == 's':
            if stay == 'h':
                print('25% Discount on groceries and books')
            elif stay == 'l':
                residencePin = int(input('Enter ur residence pin'))
                if residencePin in discountPin :
                    print('20% Discount on groceries and books')
                else:
                    print('Offer not available in this pincode')    
