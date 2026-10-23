
def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # 2. Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter (A-Z).")

    # 3. Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter (a-z).")

    # 4. Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number (0-9).")

    # 5. Check special characters
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        feedback.append("Add a special character, such as ! or @.")

    # Classify password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


print("=== Password Strength Checker ===")

password = input("Enter a password to check: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions to improve your password:")
    for suggestion in feedback:
        print("-", suggestion)
else:
    print("Great! All five checks passed.")
