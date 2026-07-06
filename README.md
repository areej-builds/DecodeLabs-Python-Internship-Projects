# Python CLI To-Do List Application

A structured, lightweight Command-Line Interface (CLI) application built with pure Python. This project focuses on implementing robust core programming logic and efficient data handling practices without relying on global state configurations.

---

## Key Features

* **Dynamic Data Insertion:** Allows users to add tasks with automatically incrementing sequential unique IDs.
* **Structured Data Representation:** Generates a clean, formatted terminal-based table output to display all records simultaneously.
* **State Modification:** Performs custom lookups by task ID to locate specific records and securely update their status to "Completed".
* **Input Validation:** Features basic exception handling to prevent empty text inputs or invalid non-numeric entries during record lookups.

---

## Technical Concepts Implemented

* **Procedural Programming:** Code architecture separated cleanly into independent, single-responsibility functions for processing and output.
* **Local State Management:** Data states are encapsulated within the main execution loop and transferred via parameters, avoiding the use of the `global` keyword.
* **Data Layer Architecture:** Implements standard data structuring by using Python dictionaries as individual database rows, appended inside a dynamic master list container.

---

## How to Run the Project

1. **Prerequisites:** Ensure that Python 3 is installed and configured on your system environment.
2. **Directory Navigation:** Open your terminal or preferred IDE terminal (e.g., VS Code) and navigate to the folder containing your project file.
3. **Execution Command:** Run the script by executing the following command:
   ```bash
   python todo_list_app.py
