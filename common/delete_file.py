import os 
 
print(os.listdir())
file = input("Input Remove File Name:")
os.remove(file)
print(os.listdir())