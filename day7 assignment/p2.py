age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female.")
occupation = input("Enter occupation :\n s student \n w working  ")
stay = input('Enter stay location : \n l locality \n h hosteller ')

if age < 45 and gender=='f' and occupation =='w' and stay=='h':
    print("50 rs coupon on nykaa product")
else:
    print('25% Discount on all products')    
if age < 45 and gender =='f' and occupation =='s' and stay=='h':
    print("100rs coupon on nykaa product and discount on book")
else:
    print('100rs Discount on all products and books') 


if age< 60 and gender =='m' and occupation =='w' and stay=='h':
    print('50% Discount on laptop and phones')   
else:
    print('25% Discount on all products')     
if age< 60 and gender =='m' and occupation =='s' and stay=='h':
    print('100rs Discount on titan and fasttrack')   
else:
    print('25% Discount on all products and books')         


if age < 45 and gender=='f' and occupation =='w' and stay=='l':
    print("50rs coupon on nykaa product")
else:
    print('25rs Discount on all products')  
if age < 45 and gender=='f' and occupation =='s' and stay=='l':
    print("50% Discount on nykaa product and discount on books")
else:
    print('25% Discount on all products and books')  


if age< 60 and gender =='m' and occupation =='w' and stay=='l':
    print('40% Discount on laptop and phones')   
else:
    print('20% Discount on all products') 
if age< 60 and gender =='m' and occupation =='w' and stay=='l':
    print('40% Discount on titan and fasttrack product')   
else:
    print('20% Discount on all products and books')             