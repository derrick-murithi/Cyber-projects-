"""
Password Strength Checker
=========================
Analyzes passwords for strength based on multiple security criteria.
Provides detailed feedback and a score to help users create stronger passwords.

Author: Your Name
License: MIT
"""

import re
import math
import string
from dataclasses import dataclass, field
from typing import List


@dataclass
class PasswordResult:
    """Holds the analysis result for a password."""
    password: str
    score: int = 0
    strength: str = ""
    entropy: float = 0.0
    passed_checks: List[str] = field(default_factory=list)
    failed_checks: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)


# Common weak passwords to flag
COMMON_PASSWORDS = {
    "password", "123456", "password1", "qwerty", "abc123",
    "letmein", "monkey", "1234567890", "dragon", "master",
    "sunshine", "princess", "welcome", "shadow", "superman"
}


def calculate_entropy(password: str) -> float:
    """
    Calculate password entropy in bits.
    Entropy = log2(pool_size ^ length) = length * log2(pool_size)
    Higher entropy = harder to brute force.
    """
    pool_size = 0
    if re.search(r"[a-z]", password):
        pool_size += 26
    if re.search(r"[A-Z]", password):
        pool_size += 26
    if re.search(r"\d", password):
        pool_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool_size += 32

    if pool_size == 0:
        return 0.0
    return len(password) * math.log2(pool_size)


def check_password_strength(password: str) -> PasswordResult:
    """
    Analyze a password across multiple security dimensions.

    Scoring:
        Each passed check awards points (max 100).
        Score 0-39:  Weak
        Score 40-59: Fair
        Score 60-79: Strong
        Score 80+:   Very Strong

    Args:
        password: The password string to evaluate.

    Returns:
        PasswordResult dataclass with score, strength label, entropy,
        passed/failed checks, and improvement suggestions.
    """
    result = PasswordResult(password=password)

    # --- Check 1: Minimum length ---
    if len(password) >= 8:
        result.score += 10
        result.passed_checks.append("Meets minimum length (8+ chars)")
    else:
        result.failed_checks.append("Too short (minimum 8 characters)")
        result.suggestions.append("Use at least 8 characters.")

    # --- Check 2: Recommended length ---
    if len(password) >= 12:
        result.score += 15
        result.passed_checks.append("Good length (12+ chars)")
    else:
        result.suggestions.append("Aim for 12+ characters for better security.")

    # --- Check 3: Excellent length ---
    if len(password) >= 16:
        result.score += 10
        result.passed_checks.append("Excellent length (16+ chars)")

    # --- Check 4: Lowercase letters ---
    if re.search(r"[a-z]", password):
        result.score += 10
        result.passed_checks.append("Contains lowercase letters")
    else:
        result.failed_checks.append("No lowercase letters")
        result.suggestions.append("Add lowercase letters (a-z).")

    # --- Check 5: Uppercase letters ---
    if re.search(r"[A-Z]", password):
        result.score += 10
        result.passed_checks.append("Contains uppercase letters")
    else:
        result.failed_checks.append("No uppercase letters")
        result.suggestions.append("Add uppercase letters (A-Z).")

    # --- Check 6: Digits ---
    if re.search(r"\d", password):
        result.score += 10
        result.passed_checks.append("Contains numbers")
    else:
        result.failed_checks.append("No numbers")
        result.suggestions.append("Include at least one number (0-9).")

    # --- Check 7: Special characters ---
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        result.score += 15
        result.passed_checks.append("Contains special characters")
    else:
        result.failed_checks.append("No special characters")
        result.suggestions.append("Add special characters (e.g., !, @, #, $).")

    # --- Check 8: No repeated characters (e.g., "aaa") ---
    if not re.search(r"(.)\1{2,}", password):
        result.score += 10
        result.passed_checks.append("No repeated character sequences")
    else:
        result.failed_checks.append("Contains repeated characters")
        result.suggestions.append("Avoid repeating the same character 3+ times.")

    # --- Check 9: Not a common password ---
    if password.lower() not in COMMON_PASSWORDS:
        result.score += 10
        result.passed_checks.append("Not a commonly used password")
    else:
        result.score -= 30
        result.failed_checks.append("This is a very common password!")
        result.suggestions.append("Choose a unique password; this one is on breach lists.")

    # --- Determine strength label ---
    result.entropy = calculate_entropy(password)
    if result.score >= 80:
        result.strength = "Very Strong 🔒"
    elif result.score >= 60:
        result.strength = "Strong 💪"
    elif result.score >= 40:
        result.strength = "Fair ⚠️"
    else:
        result.strength = "Weak ❌"

    return result


def display_result(result: PasswordResult) -> None:
    """Pretty-print the password analysis result to the console."""
    print("\n" + "=" * 50)
    print("       PASSWORD STRENGTH ANALYSIS")
    print("=" * 50)
    print(f"  Password : {'*' * len(result.password)}")
    print(f"  Length   : {len(result.password)} characters")
    print(f"  Score    : {result.score}/100")
    print(f"  Strength : {result.strength}")
    print(f"  Entropy  : {result.entropy:.2f} bits")
    print("-" * 50)

    if result.passed_checks:
        print("  ✅ Passed Checks:")
        for check in result.passed_checks:
            print(f"     • {check}")

    if result.failed_checks:
        print("  ❌ Failed Checks:")
        for check in result.failed_checks:
            print(f"     • {check}")

    if result.suggestions:
        print("  💡 Suggestions:")
        for tip in result.suggestions:
            print(f"     • {tip}")

    print("=" * 50 + "\n")


def main():
    """Interactive CLI for the password strength checker."""
    print("╔══════════════════════════════════╗")
    print("║   Password Strength Checker v1.0 ║")
    print("╚══════════════════════════════════╝")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            password = input("Enter a password to check: ").strip()
            if password.lower() == "quit":
                print("Goodbye!")
                break
            if not password:
                print("Please enter a password.\n")
                continue
            result = check_password_strength(password)
            display_result(result)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
