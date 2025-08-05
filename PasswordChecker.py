# Password Strength Checker by waleed mohamed

password = input("Enter a password: ")

if (len(password) >= 8 and
    any(char.isdigit() for char in password) and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password)):
    print("Strong password 💪")
else:
    print("Weak password ❌ - Use 8+ chars, uppercase, lowercase & numbers.")
