# Dictionary
## What is a dictionary❓❓
In python, a dictionary is an ordered collection of key-value pairs. It's a mutable data type that stores mappings of unique keys to values.

## Basic Characterstics:

- ✅ *Mutable* : A dictionary is a mutable data type, meaning it can be modified after creation.

- ✅ *Orderd* : Dicrionaries are ordered collection of key-value pairs.

- ✅ *Duplicates not allowed* ⛔ : Dictionaries do not allow duplicate keys.

## 🏗️ Creating a Dictionary:
There are several ways to create a dictionary in python:

1. Using the `{}` syntax:

```python
my_dict = {'name' : 'Jhon', 'age' : 30}
```

2. Using the `dict` constructor:

```python
my_dict = dict(name = 'Jhon', age = 30)
```

## Dictionary Operations 🩻:

### 1. Accessing Values 
You can access value using it's corresponding key:

```python
my_dict = {'name' : 'Jhon', 'age' : 30}
print(my_dict['name']) # Output : Jhon
```

### 2. Updating Values
You can update a value using its corresponding key:

```python
my_dict = {'name' : 'Jhon', 'age' : 30}
my_dict['age'] = 31
print(my_dict) # Output :  {'name' : 'Jhon', 'age' : 31}
```

### 3. Adding New key-Values Pairs
You can add a new key-value pair using the following syntax:

```python
my_dict = {'name' : 'Jhon', 'age' : 30}
my_dict['city'] = 'New York'
```

### 4. Removing Key-Value Pairs
You can remove a pair using the `del` statement:

```python
my_dict = {'name' : 'Jhon', 'age' : 30, 'city' : 'New York'}
del my_dict['city']
print(my_dict)
```