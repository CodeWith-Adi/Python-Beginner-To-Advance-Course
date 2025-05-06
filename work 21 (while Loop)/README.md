# While Loop

## Introduction
A while loop in Python repeatedly executes a block of code while a given condition is true.

## Basic Syntax
```python
while condition:
    # code block
```

## Key Points
- Loop continues as long as condition is True
- Must include a way to eventually make condition False

## Common Examples
```python
# Counter loop
count = 0
while count < 5:
    print(count)
    count += 1

# User input loop
response = ""
while response.lower() != "quit":
    response = input("Enter 'quit' to exit: ")
```

## Tips
- Avoid infinite loops
- Test your exit condition