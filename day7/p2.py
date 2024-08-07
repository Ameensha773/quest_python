age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any character.")

if age >= 60 and gender.lower() == "m":
    print("Senior citizen discount applied, thank you for shopping")
elif age >= 45 and gender.lower() == "f":
    print("Senior citizen discount applied, thank you for shopping")
else:
    print("Thank you for shopping")

if gender == 'm' and age < 60:
    print("100 voucher for fasttrack")
elif gender == 'f' and age < 45:
    print("100 voucher for nykaa")

residence = input("Enter residence:\n1.Hostellor\n2.Localite ")
if residence ==  "1":
    print("250 on groceries")
else:
    print("NA")    

occupation = input("Enter occupation:\n1.Student\n2.Working ")
if occupation ==  "1":
    print("500 coupon on books")
else:
    print("NA") 

parent_job = input("Is your parents in armed force (yes/no): ")
if parent_job == "yes":
    print("Pass for R-Day parade")
           
            
            
                