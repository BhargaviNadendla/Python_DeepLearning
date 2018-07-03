"""
Using NumPy create random vector of size 15 having only Integers in the range 0-20.
Write a program to find the most frequent item/value in the vector list.
Sample input:[1,2,16,14,6,5,9,9,20,19,18]
Sample output:Most frequent item in the list is 9
"""
import numpy as np
print(np.arange(9).reshape(3,3))
array = np.random.randint(20,50, size=15) #Generate 15 random numbers of range 0-20
print(array)
counts = np.bincount(array)  #bincount() counts no.of occurances of each value in an array of non-negative ints
print("The most frequent number is: ", np.argmax(counts)) #argmax(counts) prints the most frequent number

