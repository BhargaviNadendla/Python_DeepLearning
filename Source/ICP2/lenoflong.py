""""
1. Takes a list of words and returns the length of the longest one -the purpose here is how to take advantage of the tuples
when we are using the list.For programming this, you may want to follow the approach which take advantage of both tuple and list1.
 having two list one for your words like: ["PHP", "Exercises", "Backend"]2. another list for keeping the count of the letters in each word
  like word_len3. then iterate through the wordlist, then append the LEN of each word to the list4. you will have a list which contains
  both the word and lenof the word like this: [(3,”php),(9,”Exercises”), (7,”backend”)].5.
Then sort this list6. then return the last tuple
"""

my_words = ['Apple', 'Banana', 'Mango', 'Kiwi', 'Grapes']
words_len =[]
list_tuple = []
for i in my_words:
    words_len.append(len(i))
    list_tuple.append((len(i), i))
list_tuple.sort()
print(list_tuple[-1])