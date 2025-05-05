# Python Loop Tutorial

## Introduction to loops
Loops are fundamental programming constructs that allow you to repeat a block of code multiple times. In Python, loops help automate repetitive tasks, process collections of data, and create efficient, concise code. The two main types of loops in Python are 'for' loops and 'while' loops, with this tutorial focusing on 'for' loops.

## For loops
A 'for' loop is a control flow statement that iterates over a sequence (such as a list, tuple, string, or range) and executes a block of code for each element in the sequence. It provides a clean, efficient way to repeat code operations a specific number of times or process collections of data systematically.

## Basic Syntax
```python
for item in sequence:
    # code block to be executed
```

## Common Examples

### 1. Loop through a Range
```python
for i in range(5):
    print(i)  # prints 0, 1, 2, 3, 4
```

### 2. Loop through a List
```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```