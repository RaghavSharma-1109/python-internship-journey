s = input("Enter your string: ").lower()

for i in "!@#$%^&*,.;?": #remove punctuations basically replace only remove one at time
    s = s.replace(i, " ")

s = s.split() # using split made a list to loop through it
freq = {}

for ch in s: # counting all unique words.
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
# sorted,,,need to revise(change this when using git)
freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

for word,count in freq:# printing answer
    print(word, count)