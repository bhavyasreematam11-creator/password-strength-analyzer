import re
import getpass
import secrets
import string

# List of common passwords
common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "password123"
]


# Generate a secure random password
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):
        password += secrets.choice(characters)

    return password


# Check password strength
def check_password(password):
    score = 0
    suggestions = []

    # Check common passwords
    if password.lower() in common_passwords:
        suggestions.append(
            "This is a common password. Choose a more unique password."
        )
    else:
        score += 1

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letter
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

    # Check uniqueness / repeated characters
    if len(password) > 0:
        unique_ratio = len(set(password)) / len(password)

        if unique_ratio >= 0.6:
            score += 1
        else:
            suggestions.append(
                "Avoid using too many repeated characters. "
                "Choose a more unique password."
            )

    return score, suggestions


# Main program
password = getpass.getpass("Enter your password: ")

score, suggestions = check_password(password)

print("\nPassword Strength Analyzer")
print("--------------------------")
print("Score:", score, "/ 7")


# Display password strength
if score <= 3:
    print("Strength: Weak")
elif score <= 5:
    print("Strength: Medium")
else:
    print("Strength: Strong")


# Display suggestions
if suggestions:
    print("\nSuggestions:")

    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password meets all basic requirements!")


# Generate a secure password
print("\nSuggested secure password:")
print(generate_password())
