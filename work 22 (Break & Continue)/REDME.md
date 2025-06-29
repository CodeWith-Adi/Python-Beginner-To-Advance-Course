# Break and Continue

In Python, `break` and `continue` are powerful loop control statements that help you control the flow of your loops. Let's understand them with real-life examples.

## Break Statement
The `break` statement exits the loop completely. Think of it like:
- Leaving a shop when you find what you need
- Stopping a search when you find your lost keys

### Example:
```python
# Finding a specific number in list
numbers = [1, 3, 5, 7, 4, 8, 9, 2, 6]
search_num = 9

for num in numbers:
    if num == search_num:
        print(f"Found the number: {num}")
        break    # Stop searching once found
    print(f"Checking number: {num}")
```

## Continue Statement
The `continue` statement skips the rest of the current iteration and moves to the next one. Think of it like:
- Skipping advertisements while watching TV
- Ignoring a box of books when you know all are not from your language.

### Example:
```python
number = 1
while True:
    if number % 2 != 0:    # If number is odd
        continue    # Skip odd numbers
    print(f"Even number found: {counter}")
```

Remember: Use `break` when you want to exit the loop, and `continue` when you want to skip certain iterations.