import csv
import sys
import re
from tabulate import tabulate


menu = [
    ["1", "Display Employees List"],
    ["2", "Register New Employee"],
    ["3", "Delete Employee"],
    ["4", "Search Employee"],
    ["5", "Exit"]
]

filename = "db.csv"
FIELDNAMES = ["Employee ID", "Name", "Email", "Age", "Sex"]
def main():
    try:
        with open(filename) as file:
            reader = list(csv.reader(file))

        if not reader:
            with open(filename, "a") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()

    except FileNotFoundError:
        with open(filename, "w") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

    while True:
        print("\n\nCompany Staff Registration System")
        print(tabulate(menu, tablefmt="simple"))
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            display_employees()
        elif choice == "2":
            register_employee_menu()
        elif choice == "3":
            delete_employee_menu()
        elif choice == "4":
            search_employee_menu()
        elif choice == "5":
            sys.exit("Exiting the program. Goodbye!\n")
        else:
            print("\nInvalid choice. Please enter a valid number.")

def display_employees():
    try:
        with open(filename) as file:
            reader = list(csv.DictReader(file))
            if not reader:
                print("\nNo Employees in the database, please register an employee first")
            else: print("\n", tabulate(reader, tablefmt="heavy_outline", headers="keys"), sep="")

    except FileNotFoundError:
        sys.exit("File does not exist")

def register_employee_menu():
    print("\nAdding a new employee to the database.\n")

    while True:
        name = input("Enter Employee Name: ")
        if not name:
            print("Invalid Name")
            continue
        if re.search(r"^[a-zA-Z\s]*$", name):
            break
        else: print("Invalid Name")
    while True:
        email = input("Enter Employee Email: ")
        if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
            break
        else: print("Invalid Email")

    while True:
        try:
            age = int(input("Enter Employee Age: "))
            if 18 <= age <= 60:
                break
            else: print("Invalid Age")
        except ValueError:
            print("Invalid Age")
            pass
    while True:
        sex = input("Enter Employee sex (M|Male|F|Female): ").lower()
        if sex in ["m", "f", "male","female"]:
            if sex == "m" or sex == "male": sex = "Male"
            elif sex == "f" or sex == "female": sex = "Female"
            break
        else: print("Invalid Sex")

    try:
        with open(filename) as file:
            reader = list(csv.DictReader(file))
            if not reader:
                new_id = 1
            else:
                new_id = int(reader[-1]["Employee ID"]) + 1

        with open(filename, "a") as file:
            fieldnames = ["Employee ID", "Name", "Email", "Age", "Sex"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            newdict = {
                "Employee ID" : new_id,
                "Name" : name,
                "Email" : email,
                "Age" : age,
                "Sex" : sex,
                }
            writer.writerow(newdict)

    except FileNotFoundError:
        sys.exit("File does not exist")

def delete_employee_menu():
    try:
        with open(filename) as file:
            reader = list(csv.DictReader(file))
            while True:
                flag = False
                id = input("Enter the employee's ID to remove them from the database, or press Enter to go back to the main menu: ")
                if not id: return
                for item in reader:
                    if item["Employee ID"] == id:
                        flag = True
                if flag == True:
                    break
                print("\nID not found\n")
            new_list = [line for line in reader if line["Employee ID"] != id]

        with open(filename, "w") as file:
            fieldnames = ["Employee ID", "Name", "Email", "Age", "Sex"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_list)
            print("\nThe employee has been successfully removed.")

    except FileNotFoundError:
        sys.exit("File does not exist")

def search_employee_menu():
    try:
        with open(filename) as file:
            reader = list(csv.DictReader(file))
            result = []
            search = input("Enter employee's ID you want to search for: ")
            for item in reader:
                if item["Employee ID"] == search:
                    result.append(item)
            if result:
                print("\nSearch Results:")
                print("\n", tabulate(result, tablefmt="heavy_grid", headers="keys"), sep="")
            else: print("\nNo matching employee found.")

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
