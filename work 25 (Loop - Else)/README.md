# Loop with Else in Python

The `else` clause is executed when the loop completes normally. This is a unique feature in Python that can be used with both `for` and `while` loops.


## Example

```python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")
```

```python
count = 1
while count <= 5:
    print("hello")
    count += 1
else:
    print("Loop completed sucessfully")
```

```python
count = 1
while count <= 5:
    if count == 3:
        print("hello")
    count += 1
else:
    print("Loop completed sucessfully")
```

## Common Use Cases

1. Search operations
2. Input validation
3. Data processing completion checks

## Key Points

- The `else` block executes after the loop completes successfully
- The `else` block does not execute if the loop is terminated by a `break` statement
- Useful for search operations and validation scenarios