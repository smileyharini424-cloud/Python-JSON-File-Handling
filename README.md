# Python JSON File Handling

## Explanation

This program demonstrates how Python works with JSON (JavaScript Object Notation) data using the built-in `json` module. It creates JSON data, stores it in a file, reads the file, and displays the information.

## Problem Statement

Write a Python program to store student information in a JSON file and read the stored information using Python's `json` module.

## Features

* Creates a JSON file
* Stores structured student data
* Reads JSON data
* Converts Python data into JSON
* Displays student information

## How It Works

1. A Python dictionary containing student details is created.
2. The `json.dump()` method writes the dictionary to a JSON file.
3. The file is opened in read mode.
4. The `json.load()` method reads the JSON data.
5. The retrieved information is displayed.

## Technologies Used

* Python 3
* `json` module
* JSON files
* Dictionary

## Program Flow

Start → Create Dictionary → Write JSON File → Read JSON File → Display Data → End

## Sample Input

```text
No user input required.
```

## Sample Output

```text
Student Details:
Name: Harini
Age: 20
Course: CSE
City: Hyderabad
```

## Key Learning

* JSON is used to store structured data.
* Python provides the built-in `json` module.
* `json.dump()` writes Python data to a JSON file.
* `json.load()` reads JSON data from a file.
* Dictionaries can be easily converted to JSON.

## File Location

```text
Python-JSON-File-Handling/json_file_handling.py
```

## Repository Structure

```text
Python-JSON-File-Handling/
│
├── json_file_handling.py
├── student.json
└── README.md
```

## Author

V.Harini
