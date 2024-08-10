import shutil
import os
print(os.getcwd())
os.mkdir("source")
file=open("source/file1.txt", 'x')
file.close()
try:
   os.mkdir("destination") 
except :
    print("This file exists")   

try:
    shutil.copyfile('source/file1.txt',"destination/file2.txt")
except:
    print("No file in source")