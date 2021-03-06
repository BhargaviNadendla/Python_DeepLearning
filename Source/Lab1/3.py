"""
 Given a list of n number, write a Python program to find triplets in the list which gives the sum of zero.
 Sample input:[1, 3, 6, 2, -1, 2, 8, -2, 9]Sample output:[(3, -1, -2)]

"""
triplets = []
inp = [int(x) for x in input("Enter a list of numbers: ").split()]
for i in range(0, len(inp) - 2): #ranging from the first element to the last but 3rd element

    for j in range(i + 1, len(inp)- 1): #ranging from the first element to the last but 2nd element

        for k in range(j + 1, len(inp)): #ranging from the first element to the last but one element

            if (inp[i] + inp[j] + inp[k] == 0):
                if (inp[i], inp[j], inp[k]) not in triplets:
                    triplets.append((inp[i], inp[j], inp[k])) # if the sum is 0 and the triplet is not in list, add it

print("Triplets are" ,triplets)
