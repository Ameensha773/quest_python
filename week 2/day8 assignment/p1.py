# Get user input
name = input('Enter your name: ')
branch = input('Enter your branch (ECE, MECH, BCOM): ').upper()

# Get marks input and handle possible errors
try:
    arts = int(input('Enter the marks for Arts: '))
    maths = int(input('Enter the marks for Maths: '))
    english = int(input('Enter the marks for English: '))
except ValueError:
    print('Please enter valid numeric values for marks.')
    exit()

# Print marks for confirmation
print('Your marks are:')
marks = {'Arts': arts, 'Maths': maths, 'English': english}
print(marks)

# Get preferences input and validate
try:
    preference1 = int(input('Enter your 1st preference (1 = Marketing, 2 = Accounts, 3 = Sales): '))
    preference2 = int(input('Enter your 2nd preference (1 = Marketing, 2 = Accounts, 3 = Sales): '))
    if preference1 not in [1, 2, 3] or preference2 not in [1, 2, 3]:
        raise ValueError("Preferences must be 1, 2, or 3.")
except ValueError as e:
    print(f"{e} Please enter valid numeric values for preferences.")
    exit()

# Determine eligibility based on branch and preferences
if branch == 'ECE':
    if (preference1 == 1 or preference2 == 1) and arts > 90 and english > 90 and maths > 35:
        print('You are eligible for Marketing.')
    elif (preference1 == 2 or preference2 == 2) and arts > 35 and english > 35 and maths > 95:
        print('You are eligible for Accounts.')
    elif (preference1 == 3 or preference2 == 3) and arts > 35 and english > 90 and maths > 90:
        print('You are eligible for Sales.')
    else:
        print('You are not eligible.')

elif branch == 'BCOM':
    if (preference1 == 2 or preference2 == 2) and arts > 35 and english > 35 and maths > 95:
        print('You are eligible for Accounts.')
    elif (preference1 == 3 or preference2 == 3) and arts > 35 and english > 90 and maths > 90:
        print('You are eligible for Sales.')
    else:
        print('You are not eligible.')

elif branch == 'MECH':
    if (preference1 == 3 or preference2 == 3) and arts > 35 and english > 90 and maths > 90:
        print('You are eligible for Sales.')
    else:
        print('You are not eligible.')

else:
    print('Invalid branch selection.')
