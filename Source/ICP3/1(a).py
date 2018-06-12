"""
1. Dictionaries and setsa. Write a Python program to get the sentence from
the user and then count the frequency of each word in it using dictionary.
The words as keys should be in sorted manner in dictionary.
Display it.Input:hello world this is my first hello Output:{"first":1, "hello":2, "is":1, "my":1, "this":1, "world":1}
"""

mydict ={}
inp = input(" Enter the sentence")
words = inp.split()
mywords = sorted(words)
for word in mywords:
    mydict[word] = words.count(word)
print(mydict)
