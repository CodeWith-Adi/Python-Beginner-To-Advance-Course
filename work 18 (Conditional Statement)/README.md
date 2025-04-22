# Python Conditional Statements Tutorial

## Introduction
Conditional statements in Python allow you to execute different code blocks based on specific conditions.

## Types of Conditional Statements
1. if statement
2. if-else statement
3. if-elif-else statement

## Basic Syntax

### Simple if Statement
```python
if condition:
    # code block
```

### if-else Statement
```python
if condition:
    # code block for True
else:
    # code block for False
```

### if-elif-else Statement
```python
if condition1:
    # code block for condition1
elif condition2:
    # code block for condition2
else:
    # code block for all other cases
```

## Comparison Operators
- `==` (equal to)
- `!=` (not equal to)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)

## Examples
```python
# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

## Best Practices
- Use proper indentation
- Keep conditions simple and readable
- Use elif instead of nested if statements when possible