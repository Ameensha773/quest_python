#demonstration of different ways to add and delete an element in list

#Adding

#append method
brands=['nissan','toyota','ford']
brands.append('bmw')
print(brands)

#insert method
brands=['nissan','toyota','bmw']
brands.insert(2,'benz')
print(brands)

#extend method
brands=['nissan','bmw','toyota']
brands.extend(['bmw','audi'])
print(brands)

#Deleting

#pop method
brands=['nissan','bmw','toyota']
brands.pop(2)
print(brands)

#del method
brands=['nissan','bmw','toyota']
del brands[2]
print(brands)

#clear all method
brands=['nissan','bmw','toyota']
brands.clear()
print(brands)