# 🔐 Password Strength Checker

A Python tool that analyzes password strength across multiple security dimensions, calculates entropy, and provides actionable feedback to help users create more secure passwords.

## Features

- **Multi-factor scoring** — evaluates length, character diversity, entropy, and common password detection
- **Entropy calculation** — computes password entropy in bits (higher = harder to brute force)
- **Common password detection** — flags passwords found on breach lists
- **Actionable suggestions** — tells users exactly how to improve their password
- **Strength labels** — Weak / Fair / Strong / Very Strong

## How It Works

| Check | Points |
|---|---|
| Minimum length (8+) | +10 |
| Good length (12+) | +15 |
| Excellent length (16+) | +10 |
| Lowercase letters | +10 |
| Uppercase letters | +10 |
| Numbers | +10 |
| Special characters | +15 |
| No repeated chars | +10 |
| Not a common password | +10 / -30 |

**Strength Thresholds:**
- 🔴 0–39 → Weak
- 🟡 40–59 → Fair
- 🟢 60–79 → Strong
- 💎 80+ → Very Strong

## Usage

```bash
# Run directly
python password_checker.py
```

```python
# Use as a module
from password_checker import check_password_strength

result = check_password_strength("MyP@ssw0rd!")
print(result.score)       # 85
print(result.strength)    # Very Strong 🔒
print(result.entropy)     # 72.68 bits
print(result.suggestions) # []
```

## Example Output

```
==================================================
       PASSWORD STRENGTH ANALYSIS
==================================================
  Password : ***********
  Length   : 11 characters
  Score    : 55/100
  Strength : Fair ⚠️
  Entropy  : 72.39 bits
--------------------------------------------------
  ✅ Passed Checks:
     • Meets minimum length (8+ chars)
     • Contains lowercase letters
     • Contains uppercase letters
     • Contains numbers
     • Contains special characters
  ❌ Failed Checks:
     • No repeated characters (skipped)
  💡 Suggestions:
     • Aim for 12+ characters for better security.
==================================================
```

## Requirements

- Python 3.7+
- No external dependencies

## Concepts Demonstrated

- Password entropy mathematics
- Regular expression pattern matching
- Security scoring systems
- Breach/common password detection
