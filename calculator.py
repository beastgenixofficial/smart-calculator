from operations import add, subtract, multiply, divide, power, square_root
from calc_history import save_history, read_history


def show_menu():
    print("\n====== SMART CALCULATOR ======")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. View History")
    print("0. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    try:
        if choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = add(a, b)
            history_entry = f"{a} + {b} = {result}"

        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = subtract(a, b)
            history_entry = f"{a} - {b} = {result}"

        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = multiply(a, b)
            history_entry = f"{a} * {b} = {result}"

        elif choice == "4":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = divide(a, b)
            history_entry = f"{a} / {b} = {result}"

        elif choice == "5":
            a = get_number("Enter base number: ")
            b = get_number("Enter power: ")
            result = power(a, b)
            history_entry = f"{a} ^ {b} = {result}"

        elif choice == "6":
            a = get_number("Enter number: ")
            result = square_root(a)
            history_entry = f"√{a} = {result}"

        elif choice == "7":
            print("\n------ CALCULATION HISTORY ------")
            history = read_history()
            if not history:
                print("No history found.")
            else:
                for line in history:
                    print(line.strip())
            continue

        elif choice == "0":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice. Please select a valid option.")
            continue

        print("✅ Result:", result)
        save_history(history_entry)

    except ValueError as e:
        print("⚠️ Error:", e)
