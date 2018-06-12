mydict ={}
inp = input(" Enter the sentence")
words = inp.split() #split the sentence into a list of words

mywords = sorted(words) #sort the list
for word in mywords:
    mydict[word] = words.count(word) # find count of each word and add it to dict
print(mydict)
