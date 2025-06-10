password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
specials = "@#$"
score = 0

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char in specials:
        has_special = True

good_length = len(password) >= 8

if good_length:
    score += 2
if has_upper:
    score += 2
if has_lower:
    score += 2
if has_digit:
    score += 2
if has_special:
    score += 2

missing = []
if not good_length:
    missing.append("8 characters")
if not has_upper:
    missing.append("one uppercase letter")
if not has_lower:
    missing.append("one lowercase letter")
if not has_digit:
    missing.append("one digit")
if not has_special:
    missing.append("one special character")

if len(missing) == 0:
    print("Your password is strong! 💪")
else:
    print("Your password needs at least ", end="")
    if len(missing) == 1:
        print(missing[0] + ".")
    elif len(missing) == 2:
        print(missing[0] + " and " + missing[1] + ".")
    elif len(missing) == 3:
        print(missing[0] + ", " + missing[1] + " and " + missing[2] + ".")
    elif len(missing) == 4:
        print(missing[0] + ", " + missing[1] + ", " + missing[2] + " and " + missing[3] + ".")
    elif len(missing) == 5:
        print(missing[0] + ", " + missing[1] + ", " + missing[2] + ", " + missing[3] + " and " + missing[4] + ".")

print("Password Strength Score: ", score, "/ 10")

