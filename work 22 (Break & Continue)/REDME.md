# Break and Continue

In Python, `break` and `continue` are powerful loop control statements that help you control the flow of your loops. Let's understand them with real-life examples.

## Break Statement
The `break` statement exits the loop completely. Think of it like:
- Leaving a shop when you find what you need
- Stopping a search when you find your lost keys

### Example:
```python
# Finding a specific book in a library
books = ["Harry Potter", "Lord of the Rings", "Python Basics", "Mathematics"]
search_book = "Python Basics"

for book in books:
    if book == search_book:
        print(f"Found the book: {book}")
        break    # Stop searching once found
    print(f"Checking book: {book}")
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