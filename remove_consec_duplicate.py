string1 = input("Enter your string:").lower()

compressed = "" # to add all first of duplicate or unique char.

for i in range(len(string1) - 1):
    if string1[i] != string1[i+1]: # consecutive char.
        compressed += string1[i]

#last index is left out.
compressed += string1[-1]

print(f"Your string after removing consecutive duplicates is : {compressed}")