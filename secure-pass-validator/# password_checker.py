# password_checker.py
import getpass
import string

def is_valid_password(pw):
    """Return True if the password meets all security requirements."""
    if any(ch.isspace() for ch in pw):
        return False, "Password cannot contain spaces."
    if len(pw) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(ch.isdigit() for ch in pw):
        return False, "Add at least one number."
    if not any(ch.isupper() for ch in pw):
        return False, "Add at least one uppercase letter."
    if not any(ch.islower() for ch in pw):
        return False, "Add at least one lowercase letter."
    special_chars = set(string.punctuation)
    if not any(ch in special_chars for ch in pw):
        return False, "Consider adding a special character (e.g., !@#$%) for stronger security."
    return True, "Strong password!"

def main():
    print("Enter your password (it will not be shown):")
    while True:
        s = getpass.getpass("Enter your password: ")
        if not s:
            print("You didn't enter anything — try again.")
            continue
        valid, msg = is_valid_password(s)
        if valid:
            print("✔️  " + msg)
            break
        else:
            print("✖️  " + msg)
            print("Password rules: length ≥ 8, must include upper/lowercase letters, a number, and no spaces.")

if __name__ == "__main__":
    main()
