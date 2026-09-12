def add_expense():
    date = input("Enter date: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    file = open("expenses.txt", "a")

    file.write(date + "," + category + "," +
               str(amount) + "," + description + "\n")

    file.close()

    print("Expense added successfully!")


def view_expenses():
    try:
        file = open("expenses.txt", "r")

        print("\n===== All Expenses =====")

        for line in file:
            data = line.strip().split(",")

            print("Date:", data[0])
            print("Category:", data[1])
            print("Amount:", data[2])
            print("Description:", data[3])
            print("----------------------")

        file.close()

    except FileNotFoundError:
        print("No expenses found.")


def total_expense():
    total = 0

    try:
        file = open("expenses.txt", "r")

        for line in file:
            data = line.strip().split(",")
            total = total + float(data[2])

        file.close()

        print("\nTotal Expense:", total)

    except FileNotFoundError:
        print("No expenses found.")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()
