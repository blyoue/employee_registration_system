import pytest
import csv
from project import display_employees, register_employee_menu, delete_employee_menu, search_employee_menu, main

# Assuming the filename variable is defined in employee_system.py
FILENAME = "db.csv"

def get_employee_data():
    with open("db.csv") as file:
        reader = list(csv.DictReader(file))
        print(reader)
        return reader

def test_register_employee_menu(monkeypatch, capsys):
    # Mock user input
    inputs = ["blue", "blue@gmail.com", "25", "Male"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    register_employee_menu()
    # Get the employee data from the CSV file
    employee_data = get_employee_data()


    # Check if the new employee information is present in the data
    assert {'Employee ID': '1', 'Name': 'blue', 'Email': 'blue@gmail.com', 'Age': '25', 'Sex': 'Male'} in employee_data

def test_search_employee_menu(monkeypatch, capsys):
    inputs = ["1"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    search_employee_menu()
    captured = capsys.readouterr()
    assert "Search Result" in captured.out

def test_delete_employee_menu(monkeypatch, capsys):
    inputs = ["1"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    delete_employee_menu()
    captured = capsys.readouterr()
    assert "The employee has been successfully removed." in captured.out  # Adjust based on actual output
