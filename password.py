import re

def check_password_strength(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    strength = sum(criteria.values())
    feedback = []

    if not criteria['length']:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria['uppercase']:
        feedback.append("Password should include at least one uppercase letter.")
    if not criteria['lowercase']:
        feedback.append("Password should include at least one lowercase letter.")
    if not criteria['digit']:
        feedback.append("Password should include at least one digit.")
    if not criteria['special']:
        feedback.append("Password should include at least one special character.")

    if strength == 5:
        strength_level = "Strong"
    elif strength >= 3:
        strength_level = "Medium"
    else:
        strength_level = "Weak"

    return strength_level, feedback

# Example usage
password = input("Enter a password whose strength you want to check: ")
strength_level, feedback = check_password_strength(password)

print(f"Password Strength: {strength_level}")
if feedback:
    print("Feedback:")
    for f in feedback:
        print(f"- {f}")
