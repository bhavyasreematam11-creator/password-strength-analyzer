import re
import getpass
common_passwowrds=["password","123456","12345678","qwerty","admin","password123"]
def check_password(password):
    score = 0
    suggestions = []

    if password.lower() in common_passwords:
        score=0
        suggestions.append("This is a common password. Choose a more unique password.")

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    return score, suggestions


password = getpass.getpass("Enter your password: ")

score, suggestions = check_password(password)

print("\nPassword Strength Analyzer")
print("--------------------------")
print("Score:", score, "/ 5")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password meets all basic requirements!")

