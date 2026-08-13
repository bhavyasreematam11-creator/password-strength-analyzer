import re
import getpass
import secrets
import string

common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "password123"
]


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):
        password += secrets.choice(characters)

    return password


def check_password(password):
    score = 0
    suggestions = []

    # Common password check
    if password.lower() in common_passwords:
        suggestions.append("This is a common password. Choose a more unique password.")
    else:
        score += 1

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special character check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Uniqueness check
    if len(password) > 0:
        unique_ratio = len(set(password)) / len(password)

        if unique_ratio >= 0.6:
            score += 1
        else:
            suggestions.append(
                "Avoid too many repeated characters. Choose a more unique password."
            )

    return score, suggestions


def main():
    while True:
        print("\n==============================")
        print(" PASSWORD STRENGTH ANALYZER")
        print("==============================")
        print("1. Check Password Strength")
        print("2. Generate Secure Password")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            password = getpass.getpass("Enter your password: ")

            score, suggestions = check_password(password)

            print("\nPassword Strength Analyzer")
            print("--------------------------")
            print("Score:", score, "/ 7")

            if score <= 3:
                print("Strength: Weak")
            elif score <= 5:
                print("Strength: Medium")
            else:
                print("Strength: Strong")

            if suggestions:
                print("\nSuggestions:")
                for suggestion in suggestions:
                    print("-", suggestion)
            else:
                print("\nYour password meets all basic requirements!")

        elif choice == "2":
            print("\nSuggested Secure Password:")
            print(generate_password())

        elif choice == "3":
            print("\nThank you for using Password Strength Analyzer!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


main()
