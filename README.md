# YOUR PROJECT TITLE
#### Description:

# Company Staff Registration System

## Introduction

Welcome to the Company Staff Registration System! This project is a culmination of my learning journey in the CS50P course, a comprehensive Python programming course offered by Harvard University. Throughout this course, I've gained valuable insights into the world of Python development, honing my skills in coding, problem-solving, and project development.

## Overview

The Company Staff Registration System is a Python-based command-line application designed for efficient employee information management within a company. Users can perform various operations such as displaying the employee list, registering new employees, deleting existing employees, and searching for specific employee details. The system utilizes a CSV file (`db.csv`) for persistent data storage, ensuring seamless management of employee records.


The Company Staff Registration System showcases my proficiency in Python, encompassing various aspects of the language, including file handling, input validation, and external library integration. This project aims to provide a practical solution for managing employee information within a company, emphasizing usability and efficiency.


## Functionality

### 1. Display Employees List

The `display_employees` function provides a user-friendly display of all registered employees. If the database is empty, a clear message prompts users to register an employee first. The tabulated format, courtesy of the `tabulate` library, ensures a neat and organized presentation.

### 2. Register New Employee

The `register_employee_menu` function guides users through adding a new employee to the database. Users input the employee's name, email, age, and sex, with input validation in place to ensure accurate information. The system generates a unique Employee ID for each entry, maintaining order in the database.

### 3. Delete Employee

In the `delete_employee_menu` function, users can remove an employee by entering their ID. The system offers an option to cancel the deletion by pressing Enter, enhancing user experience. Upon successful deletion, a confirmation message is displayed, and the CSV file ensures persistent data storage.

### 4. Search Employee

The `search_employee_menu` function enables users to search for a specific employee by entering their ID. If a match is found, detailed information about the employee is displayed, streamlining access to specific employee data.

## File Structure

- **project.py**: Contains the core logic of the Company Staff Registration System, including main menu, display, registration, deletion, and search functionalities.

- **test_project.py**: Houses pytest test cases to validate the functionality of core functions in `project.py`.

- **db.csv**: A CSV file serving as a persistent data store for employee information. It is initialized with headers (`Employee ID`, `Name`, `Email`, `Age`, `Sex`) if it does not exist.

## Design Choices

- **CSV Storage**: The decision to use a CSV file for data storage provides a simple and portable solution for persisting employee information. This approach is suitable for small to medium-sized databases.

- **User-Friendly Interface**: Emphasis on simplicity and clarity in the main menu and user prompts ensures a positive user experience. Input validation guides users in providing accurate information.

- **External Libraries**: The project incorporates external libraries such as `tabulate` for improved data presentation and `pytest` for automated testing. These libraries enhance the functionality and reliability of the system.

## Summary

The Company Staff Registration System offers a robust solution for managing employee information. Its intuitive interface, coupled with input validation and clear feedback, ensures a seamless experience for users. The use of a CSV file for data storage provides portability and simplicity, making it suitable for businesses of various sizes. The integration of external libraries enhances the system's functionality and reliability. This README.md provides a comprehensive guide, covering the system's functionality, file structure, design choices, and a summary, ensuring users and developers have a thorough understanding of the project.
