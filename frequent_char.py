s = input("Enter your string: ").replace(" ", "").lower()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

max_char = max(freq, key=freq.get)  # character with max frequency
max_count = freq[max_char]          # frequency of that character

print(f"Most frequent character is '{max_char}' → {max_count} times")
