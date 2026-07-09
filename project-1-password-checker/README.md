# Project 1: Password Strength Checker

**Track:** Defensive Logic-Security Fundamentals
**Skills:** String handling, conditional logic, entropy/validation basics

## Objective

Build a Python program that evaluates whether a password is Weak, Medium, or Strong based on length and character variety (uppercase, lowercase, digits, symbols).

## Approach

The checker validates two dimensions:
1. **Length** — passwords under 8 characters are automatically classified Weak, regardless of complexity (protects against brute-force risk on short strings).
2. **Character variety score** — counts how many of 4 categories are present (uppercase, lowercase, digit, symbol). 3+ categories at sufficient length = Strong.

```python
import re

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 8:
        return "Weak ❌ (too short — must be at least 8 characters)"
    elif length >= 8 and score >= 3:
        return "Strong ✅ (good length + mix of character types)"
    elif length >= 8 and score == 2:
        return "Medium ⚠️ (decent length, but add more variety)"
    else:
        return "Weak ❌ (add uppercase, numbers, or symbols)"
```

## Test Results

| Password | Result |
|---|---|
| `abc123` | Weak ❌ (too short) |
| `Password1` | Strong ✅ (3/4 categories, 8+ chars) |
| `P@ssw0rd!23` | Strong ✅ |
| `12345678` | Weak ❌ (only digits) |
| `Str0ng&Secure99` | Strong ✅ |

See [`screenshots/`](./screenshots) for the full Colab run, including interactive password testing.

## Key Learning / Limitation Noted

`Password1` scores as **Strong** under this logic (hits 3 of 4 character categories at 8+ characters), even though it's a fairly guessable, dictionary-based password in practice. This highlights a real limitation of simple category-counting checks: **character variety alone doesn't measure true unpredictability (entropy)** — a more robust checker would also screen against common/leaked password lists, not just structural rules.

## Files

- [`password_checker.py`](./password_checker.py) — full source
- [`screenshots/`](./screenshots) — Colab execution evidence
