"""
b. Use sets to count the number of vowels in a string (vowels in English are a, e, i, o, u)
[think of a solution where we can get the count of vowels even if they are duplicated]
Input:Python Program Output:Count of vowels is 3
"""
count =0
inp = input("Enter a string")

for i in inp:

    if i in set("aeiouAEIOU"):
        count = count+1
print("Vowel count is " +str(count))