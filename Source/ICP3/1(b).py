count =0
inp = input("Enter a string")

for i in inp: # for each character in string

    if i in set("aeiouAEIOU"): # if it belongs to vowel list either uppercase or lower case
        count = count+1
print("Vowel count is " +str(count))