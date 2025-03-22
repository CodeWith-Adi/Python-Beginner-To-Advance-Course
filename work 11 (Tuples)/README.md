# Tuples Tutorial

## What is a Tuple?
A tuple is an immutable, ordered collection of elements in Python. Tuples are similar to lists, but they cannot be changed after creation.

## Syntax
```python
# Creating a tuple
my_tuple = (1, 2, 3)
```

## Key Features
- **Immutable**: Once created, elements cannot be modified.
- **Ordered**: Elements maintain their order.
- **Allows Duplicates**: Tuples can contain duplicate values.

## Common Operations
### Indexing
```python
my_tuple = (10, 20, 30)
print(my_tuple[1])  # Output: 20
```

### Slicing
```python
print(my_tuple[0:2])  # Output: (10, 20)
```

### Length
```python
print(len(my_tuple))  # Output: 3
```

### Concatenation
```python
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2  # Output: (1, 2, 3, 4)
```

## Important Methods for Tuples

### `count()`
Returns the number of times a specified value appears in the tuple.
```python
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # Output: 2
```

### `index()`
Returns the index of the first occurrence of a specified value.
```python
my_tuple = (10, 20, 30)
print(my_tuple.index(20))  # Output: 1
```

### `max()`
Returns the largest element in the tuple.
```python
my_tuple = (5, 10, 15)
print(max(my_tuple))  # Output: 15
```

### `min()`
Returns the smallest element in the tuple.
```python
my_tuple = (5, 10, 15)
print(min(my_tuple))  # Output: 5
```

### `sum()`
Returns the sum of all elements in the tuple (only works with numeric values).
```python
my_tuple = (1, 2, 3)
print(sum(my_tuple))  # Output: 6
```

For better understanding watch this video : https://youtu.be/k3mYT1V75t4