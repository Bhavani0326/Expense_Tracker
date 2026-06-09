expenses = []

def add_expense():
    date = input("Enter Date: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense Added Successfully")


def view_expenses():

    if len(expenses) == 0:
        print("No Expenses Found")
        return

    for expense in expenses:
        print("---------------------")
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])
        print("Description:", expense["description"])


def total_expense():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense =", total)


def search_category():

    category = input("Enter Category: ")

    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print(expense)
            found = True

    if not found:
        print("No Expense Found")


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search Category")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        search_category()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")