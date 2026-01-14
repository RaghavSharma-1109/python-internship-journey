def is_palindrome(num):
    if num < 0:
        return False

    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev == original

num = int(input('Enter your number:'))
result = is_palindrome(num)
print(result)
