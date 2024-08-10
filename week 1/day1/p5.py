#Check if a number is single digit or not

number = int(input("Enter a number: "))

if (number <= 9 and number >= -9):
    print("number is a single digit.")
else:
    print("number is not a single-digit number.")