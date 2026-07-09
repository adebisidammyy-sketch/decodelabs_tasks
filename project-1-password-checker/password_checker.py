"""
Password Strength Checker
DecodeLabs Industrial Training Kit — Project 1
Author: Damilola
"""


def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 8:
        return "Weak \u274c (too short \u2014 must be at least 8 characters)"
    elif length >= 8 and score >= 3:
        return "Strong \u2705 (good length + mix of character types)"
    elif length >= 8 and score == 2:
        return "Medium \u26a0\ufe0f (decent length, but add more variety)"
    else:
        return "Weak \u274c (add uppercase, numbers, or symbols)"


if __name__ == "__main__":
    test_passwords = [
        "abc123",
        "Password1",
        "P@ssw0rd!23",
        "12345678",
        "Str0ng&Secure99",
    ]

    for pwd in test_passwords:
        print(f"Password: {pwd:<20} -> {check_password_strength(pwd)}")

    # Interactive check
    user_password = input("\nEnter a password to check: ")
    print(check_password_strength(user_password))
