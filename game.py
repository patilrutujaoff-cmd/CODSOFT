import random

print("===== ROCK PAPER SCISSORS GAME =====")

user_score = 0
computer_score = 0

while True:
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "4":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break

    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice")
        continue

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    user_choice = choices[int(user_choice) - 1]

    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1
