
TODO:
Create a Python function that takes a list of dictionaries as input, filters out dictionaries where a specified key has a None or Null value, and then calculates and returns the average value of another specified numerical key for the remaining dictionaries.

EXAMPLE_INPUT:
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': None},
    {'name': 'Charlie', 'age': 40},
    {'name': 'David', 'age': 35}
]


OBJETIVES
Define a Python function with appropriate parameters.
Filter out entries where the 'age' key has a None value.
Calculate the average age of the remaining entries.

NOTES
Do not use external libraries; the task should be solved using Python's standard library.
This task tests basic data manipulation and structure understanding in Python



MY ASSUMPTIONS:
- I assumed that all keys are strings
- I assumed that user could be enter something wrong so handled possible exceptions
