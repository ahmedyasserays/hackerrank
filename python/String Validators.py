s = input()
has_alnum = has_alpha = has_digit = has_lower = has_higher = False
for i in s:
    if i.isalnum():
        has_alnum = True
    if i.isalpha():
        has_alpha = True
    if i.isdigit():
        has_digit = True
    if i.islower():
        has_lower = True
    if i.isupper():
        has_higher = True
print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_higher)