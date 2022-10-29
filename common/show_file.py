import os

print(os.listdir())
file = input("Read File Name:")
lines = open(file)

for each_lines in lines:
    each_lines = each_lines.strip() #刪除字串的首尾字符
    print(each_lines + "\n")
