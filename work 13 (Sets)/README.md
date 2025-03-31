# Sets

Sets in Python are unordered collections of unique elements. 

## Creating a list :
They are defined using curly braces `{}` or the `set()` constructor.

```python
# Using curly braces
set1 = {1, 2, 3, 4, 5}

# Using set() constructor
set2 = set([1, 2, 3, 4, 5])
set3 = set("Hello")  # Creates a set of unique characters: {'H', 'e', 'l', 'o'}
```

## Key Features

- No duplicate elements
- Unordered
- Mutable
- Can contain different data types

## On what bases sets change the index of elements.

Sets automatically sort elements based on data type priority.
```python
my_set = {"apple", 2, True, "banana", 1, False}
# Output: {False, True, 2, 'apple', 'banana'}
```
In this example, strings come first, followed by numbers, and then boolean values.


## Basic Operations

```python
# Creating a set - Using curly braces for direct initialization
numbers = {1, 2, 3, 4, 5}
# Creating a set - Using set() constructor with a list
fruits = set(['apple', 'banana', 'orange'])

# Adding elements - Adds a single element to the set
numbers.add(6)

# Removing elements - Removes specified element, raises KeyError if not found
numbers.remove(1)

# Removing all elements - Removes all elements from the set
numbers.clear()  # Removes all elements from the set
```

## Set operations

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (|) - Combines elements from both sets, removing duplicates
union_set = set1 | set2
# Result: {1, 2, 3, 4, 5}

# Intersection (&) - Keeps only elements present in both sets
intersection_set = set1 & set2
# Result: {3}

# Difference (-) - Keeps elements from first set that are not in second set
difference_set = set1 - set2
# Result: {1, 2}
```