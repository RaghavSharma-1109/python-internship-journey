from math import inf


def max_digit_freq(num):
    num = abs(num)
    freq = {}

    if num == 0:
        return {0: 1}

    while num > 0:
        digit = num % 10
        freq[digit] = freq.get(digit, 0) + 1
        num //= 10
    max_freq = float('-inf')
    max_digit = float('-inf')
    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            max_digit = key

    return (max_digit, max_freq)


num = int(input("Enter a number:"))
result = max_digit_freq(num)
print(result)

    