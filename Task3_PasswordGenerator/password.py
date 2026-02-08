import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("Password length should be at least 4")
            continue

        print("\nChoose password complexity:")
        print("1. Letters only")
        print("2. Letters + Numbers")
        print("3. Letters + Numbers + Symbols")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            characters = string.ascii_letters

        elif choice == "2":
            characters = string.ascii_letters + string.digits

        elif choice == "3":
            characters = string.ascii_letters + string.digits + string.punctuation

        else:
            print("Invalid choice")
            continue

        password = "".join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (y/n): ")
        if again.lower() != "y":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")
