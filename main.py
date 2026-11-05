
import string
import secrets


def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


def generate_password(length=16):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def main():
    print("=" * 40)
    print("       CYBERSHIELD")
    print("  PASSWORD SECURITY ANALYZER")
    print("=" * 40)

    password = input("\nEnter your password: ")

    strength, suggestions = check_password(password)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nAll basic password checks passed!")

    print("\nGenerated Password:", generate_password())

    print("\nThank you for using CyberShield!")


if __name__ == "__main__":
    main()
