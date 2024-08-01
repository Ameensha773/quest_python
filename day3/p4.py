#find 1-n+n(2)-n(3)+...m terms
n = int(input("Enter the value of n: "))
m = int(input("Enter the number of terms m: "))

def calculate_sum(n, m):
    series_sum = 0
    for i in range(m):
        term = (n ** i) * ((-1) ** i)
        series_sum += term
    return series_sum

# Calculate the sum of the series
sum_of_terms = calculate_sum(n, m)

# Output the result
print("The sum of the series is:", sum_of_terms)