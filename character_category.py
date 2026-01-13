s = input("Enter your string: ")
# initialize a dict to store count
category = {'upper_case' : 0,'lower_case' : 0,'digit' : 0,'special_char': 0,'spaces' : 0} 

# find diff category of char and store it
for ch in s:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        category['upper_case'] += 1
    elif ch in "abcdefghijklmnopqrstuvwxyz":
        category['lower_case'] += 1
    elif ch in "0123456789":
        category['digit'] += 1
    elif ch in " ":
        category['spaces'] += 1
    elif ch in "!@#$%^&*":
        category['special_char'] += 1

#print all category.
for ch in category:
    print(ch, category[ch], sep="=")