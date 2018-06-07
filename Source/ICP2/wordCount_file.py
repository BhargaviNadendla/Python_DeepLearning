from collections import *
file = open('C:/Users/Bhargavii Nadendla/Desktop/myfile.txt', 'r')

lines = file.read().splitlines()
print(lines)
print(lines)
f= open("C:/Users/Bhargavii Nadendla/Desktop/outputfile.txt","w+")

for i in lines:
    f.write("{},{}\n".format(i,len(i.split())))