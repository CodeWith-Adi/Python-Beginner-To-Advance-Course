# Ternary Operator in Python

The ternary operator is a shorthand way to write an if-else statement in a single line.

## Syntax
```python
value_if_true if condition else value_if_false
```

## Example
```python
# Traditional if-else
age = 18
if age >= 18:
    status = "Adult"
    print(status)
else:
    status = "not an adult"
    print(status)

# Using ternary operator
status = "Adult" if age >= 18 else "not an adult"
```

## Benefits
- More concise code
- Improved readability for simple conditions
- Useful for quick variable assignments

## Best Practices
- Use for simple conditions only
- Avoid nested ternary operators
- Keep the expressions short and clear