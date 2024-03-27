# Calculator History Management
This Python module provides a simple interface for managing a history of calculations. It uses the pandas library to read and write calculation data to a CSV file. The module demonstrates the use of the Facade Pattern to simplify interactions with complex data manipulations and employs a basic logging strategy for monitoring actions and errors.

## Setup Instructions

### 1. Clone the Repository
    git clone repo_link

### 2. Install Dependencies: 
    pip install -r requirements.txt

### 3. Environment variable:
    create .env file and add the key value pair (FILE_PATH = './data/calc_history.csv')
[link for usage](https://github.com/Abishek183/mid_calc/blob/dev/app/history/__init__.py)

### 4. Code Execution:
    Run the main.py file by the command "python main.py"


## Usage Examples
After running the main.py file used the 'menu' command to get list of registered commands

### Addtion operation
1. Type the command 'add' in the REPL command interface
2. Enter the number when asked in the interface
3. It computes and prints the result.
[link](https://github.com/Abishek183/mid_calc/blob/dev/app/plugins/add/__init__.py)
### example
    >>>add
    enter the first number: 5
    enter the second number: 4
    9.0

### Other operation similar to Addition
1. sub - for subtraction
2. mul - for multiplication
3. div - for division

### Commands for history management
#### 1. fetch - it gets all the data from the .csv file
    >>> fetch
    data history of calculator:
    ID action  value1  value2
    1    mul     3.0     2.0
    2    div     6.0     2.0
    3    div     6.0     0.0
#### 2. clear - it deletes the history stored.
    >>> clear
    History cleared

#### 3. delete - it deletes particular row in the history by the ID field. [link](https://github.com/Abishek183/mid_calc/blob/dev/app/history/__init__.py)
    >>> delete
    enter the id for record to delete:1
    data history of calculator after delete:
    ID action  value1  value2
    2    mul     3.0     2.0
    3    div     6.0     2.0
    4    div     6.0     0.0

## Design pattern

### 1. Facade Pattern:
The History class acts as a facade by providing a simplified interface for interacting with CSV files using pandas. The methods write, read_as_list, read_as_data_frame, and clear offer a straightforward way to perform operations on the CSV file without needing to know about pandas or file handling.
[link](https://github.com/Abishek183/mid_calc/blob/dev/app/history/__init__.py)

### 2. Command Pattern:
The execute method in your command handling code is an example of the Command pattern. Each command (e.g., add, sub, etc.) can be thought of as an object that encapsulates the operation to be performed.
[link](https://github.com/Abishek183/mid_calc/blob/dev/app/plugins/add/__init__.py)

### 3. Factory Method Pattern:
The load_plugin method in the app's __init__.py file dynamically load the new plugins without any need of configurations. This is an example for factory method pattern.
[link](https://github.com/Abishek183/mid_calc/blob/dev/app/__init__.py)

### 4. Singleton Pattern:
The 'MenuCommand" is an example of singleton pattern where only one instance of it is created throughout the application.
[link](https://github.com/Abishek183/mid_calc/blob/dev/app/__init__.py)

## Logging Strategy
The module uses Python's built-in logging library to log informational messages and errors. This helps in monitoring the actions performed by the module and troubleshooting issues.

### 1. Initialization: 
The logging system is initialized at the start of the application, typically in the main module or the entry point of the application. This can be done by configuring the logging level, format, and optionally, the output destination (e.g., console, file).
[log config](https://github.com/Abishek183/mid_calc/blob/dev/logging.conf)

### 2. Usage: 
Throughout the application, logging is used to record informational messages, warnings, and errors. For example, in the History class, logging is used to inform about the creation of a directory or to log an error if the directory is not writable.

### 3. Error Handling: 
In methods where exceptions might occur (e.g., file operations, calculations), logging is used to record the error details.
[link for usage and error handling](https://github.com/Abishek183/mid_calc/blob/dev/app/__init__.py)

## EAFP (Easier to Ask for Forgiveness than Permission):
The try/except mechanism in Python is a key tool for implementing the EAFP approach. It allows you to attempt an operation and define how to handle specific exceptions if they occur. This approach is often considered more "Pythonic" and can lead to cleaner and more readable code, especially in situations where exceptions are expected or common.
[link for EAFP Implemantation](https://github.com/Abishek183/mid_calc/blob/dev/app/plugins/div/__init__.py)

## VIDEO DEMO - [HERE](https://drive.google.com/file/d/1DiQ7-QY-adaYlSCaWtQW1ymF2PwvQtCY/view?usp=sharing)