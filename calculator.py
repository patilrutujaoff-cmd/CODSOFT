print("===== SMART PYTHON CALCULATOR =====")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")
        print("x  Exit")

        choice = input("Enter operation: ")

        if choice == "+":
            print("Result:", num1 + num2)

        elif choice == "-":
            print("Result:", num1 - num2)

        elif choice == "*":
            print("Result:", num1 * num2)

        elif choice == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero is not allowed")

        elif choice.lower() == "x":
            print("Exiting Calculator. Thank you!")
            break

        else:
            print("Invalid operation. Please try again.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
