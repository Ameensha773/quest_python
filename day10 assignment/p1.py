class Customer:
    def __init__(self, age, occupation, stay):
        self.age = age
        self.occupation = occupation
        self.stay = stay

class Female(Customer):
    def check_discount(self):
        if self.age < 45:
            if self.occupation == 'w':
                if self.stay == 'h':
                    print("₹100 coupon on Nykaa product")
                elif self.stay == 'l':
                    print("₹50 coupon on Nykaa product")
            elif self.occupation == 's':
                if self.stay == 'h':
                    print("₹100 coupon on Nykaa product and discount on books")
                elif self.stay == 'l':
                    print("50% Discount on Nykaa product and discount on books")
        elif self.age >= 45:
            if self.occupation == 'w':
                if self.stay == 'h':
                    print('75% Discount on groceries')
                elif self.stay == 'l':
                    print('₹75 Discount on groceries')
            elif self.occupation == 's':
                if self.stay == 'h':
                    print('₹100 Discount on groceries and books')
                elif self.stay == 'l':
                    print('25% Discount on groceries and books')

class Male(Customer):
    def check_discount(self):
        if self.age < 60:
            if self.occupation == 'w':
                if self.stay == 'h':
                    print('50% Discount on laptops and phones')
                elif self.stay == 'l':
                    print('40% Discount on laptops and phones')
            elif self.occupation == 's':
                if self.stay == 'h':
                    print('₹100 Discount on Titan and Fastrack')
                elif self.stay == 'l':
                    print('40% Discount on Titan and Fastrack products')
        elif self.age >= 60:
            if self.occupation == 'w':
                if self.stay == 'h':
                    print('25% Discount on groceries')
                elif self.stay == 'l':
                    print('20% Discount on groceries')
            elif self.occupation == 's':
                if self.stay == 'h':
                    print('25% Discount on groceries and books')
                elif self.stay == 'l':
                    print('20% Discount on groceries and books')

    # Get user input
age = int(input("Enter age: "))
gender = input("Enter gender:\n M. Male\n F. Female\n").strip().lower()
occupation = input("Enter occupation:\n s student \n w working  ").strip().lower()
stay = input("Enter stay location:\n l locality \n h hostel ").strip().lower()

if gender == 'f':
    customer = Female(age, occupation, stay)
elif gender == 'm':
    customer = Male(age, occupation, stay)
else:
    print("Invalid gender input.")
    
customer.check_discount()

