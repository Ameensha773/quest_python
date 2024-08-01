#print the smallest and biggest size string in list of n strings

string = list(input("Enter some strings : ").split())
print (string)
longest = max(string, key=len)
shortest = min(string, key=len)
print('Shortest string:', shortest)
print('longest string:', longest)