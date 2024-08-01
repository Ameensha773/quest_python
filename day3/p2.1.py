import math
# Read the number N from the
N = int(input("Enter a number: "))

# Assume N is a prime number
prime = True

# Loop from 2 to the ceiling of the square root of N
for i in range(2, math.ceil(math.sqrt(N)) + 1):
    if N % i == 0:
        # N is not a prime number
        print(f"{N} is not a prime number.")
        prime = False
        break  # Exit the loop

# Check if the number is still considered prime
if prime:
    print(f"{N} is a prime number.")