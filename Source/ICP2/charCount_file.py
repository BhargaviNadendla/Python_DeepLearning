"""
2. Read a file which contains one word in each line.
Then Calculate the character frequency in each line. Write down the result in another file.
"""

infile = open('C:/Users/Bhargavii Nadendla/Desktop/myfile.txt', 'r')

line = infile.read().splitlines()


f= open("C:/Users/Bhargavii Nadendla/Desktop/outfile.txt","w+")
for i in line:
    length = len(i)
    f.write("{}, {}\n".format(i,length))


