s = input("Enter your Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*"

# checking for strong password
for p in s:
    if p.isupper():
        has_upper = True
    elif p.islower():
        has_lower = True
    elif p.isdigit():
        has_digit = True
    elif p in special_characters:
        has_special = True
    
if len(s) >= 8 and has_digit and has_lower and has_special and has_upper:
    print(f"Your Password ({s}) is strong.")
else:
    print(f"Your Password ({s})is weak")
