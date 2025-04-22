# 10 Python functions you must know:

## 1. input()
The `input()` function in Python allows you to accept user input from the keyboard during program execution. It displays an optional prompt message and waits for the user to type something and press Enter. By default, input() returns the entered value as a string, regardless of what type of data the user enters.

```python
# Example of input() function
name = input("What is your name? ")
age = int(input("How old are you? "))  # Converting string to integer
print(f"Hello {name}, you are {age} years old!")
```

## 2. len() 
The `len()` function returns the length (number of items) in an object. It can be used with strings, lists, tuples, dictionaries, and other sequence or collection objects. For strings, it counts the number of characters.

```python
# Example of len() function
text = "Hello World"
numbers = [1, 2, 3, 4, 5]
print(len(text))        # Output: 11
print(len(numbers))     # Output: 5
```

## 3. range()
The `range()` function generates a sequence of numbers. It's commonly used in for loops and can take up to three parameters: start, stop, and step. If only one parameter is provided, it's treated as the stop value, with start defaulting to 0 and step to 1.

```python
# Example of range() function
for i in range(5):          # 0 to 4
    print(i)

for i in range(2, 6):      # 2 to 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

## 4. max()
The `max()` function returns the largest item in an iterable or the largest of two or more arguments. It can be used with numbers, strings, and other comparable objects.

```python
# Example of max() function
numbers = [10, 5, 20, 15]
print(max(numbers))        # Output: 20
print(max(3, 7, 2))       # Output: 7
print(max("apple", "banana")) # Output: "banana"
```

## 5. min()
The `min()` function returns the smallest item in an iterable or the smallest of two or more arguments. It works similarly to max() but returns the minimum value.

```python
# Example of min() function
numbers = [10, 5, 20, 15]
print(min(numbers))        # Output: 5
print(min(3, 7, 2))       # Output: 2
```

## 6. sum()
The `sum()` function adds all items in an iterable (like a list of numbers) and returns the total.

```python
# Example of sum() function
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))        # Output: 15
print(sum([1.5, 2.5, 3.0]))  # Output: 7.0
```

## 7. abs()
The `abs()` function returns the absolute value of a number, removing any negative sign.

```python
# Example of abs() function
print(abs(-5))        # Output: 5
print(abs(-3.14))     # Output: 3.14
```

## 8. pow()
The `pow()` function returns a number raised to a specified power. It takes two arguments: the base and the exponent.

```python
# Example of pow() function
print(pow(2, 3))      # Output: 8
print(pow(5, 2))      # Output: 25
```

## 9. round()
The `round()` function rounds a floating-point number to a specified number of decimals.

```python
# Example of round() function
print(round(3.14159, 2))  # Output: 3.14
print(round(5.6))         # Output: 6
```

## 10. sorted()
The `sorted()` function returns a new sorted list from an iterable. It can sort in ascending or descending order.

```python
# Example of sorted() function
numbers = [3, 1, 4, 1, 5, 9, 2]
print(sorted(numbers))           # Output: [1, 1, 2, 3, 4, 5, 9]
print(sorted(numbers, reverse=True))  # Output: [9, 5, 4, 3, 2, 1, 1]
```