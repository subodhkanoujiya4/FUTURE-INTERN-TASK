import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "You must select at least one type of character to include in the password."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the desired password length: "))

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
