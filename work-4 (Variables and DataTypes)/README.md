# Variables and Data Types in Python 

## Variables:
Variables are like containers that store data. They are exactly like containers in your home. 
<br>
The value of a variable is stored in your computer's memory with an address. The variable is like a short and simple name for that address.

### Short Definition of Variables:
A variable is a named storage location that holds a value.

### Long Definition of Variables:
A variable is a symbolic representation of a storage location in memory that holds a value of a specific data type, which can be changed, updated, or manipulated.

### Criteria for Defining Variables in Python:
While defining variables in Python, we should keep these things in mind:
- You don't need to specify the data type of the variable. Python will automatically detect it based on the assigned value.
- The first character of your variable should be a letter.
- Choose a unique name for every variable in a program.
- Only use valid characters like letters (a to z, A to Z), digits (0 - 9), and underscores (_).

### Difining a variable in Python:
To difine a variable in python, you can use the following syntax:
```python
variable_name = value
```
on left hand side give the name of variable and in beetween put the assingment operator (=) and then give the value on the right hand side.

Example:
```python
name = "Adi"
age = 25
height = 24.3
ismale = True
# for printing these variables to console use:
print(name)
print(age)
print(height)
print(ismale)
# or
print(name, age, height, ismale)
#note do not use print("name"), quotes denote that you want name literally.
```

## Data Types:
If one the box of your home contains sugar and another contains shampoo then the both of these are acting like a variable, and the types of products stored in it are it's product type. Simmilarly, The type of data stored in a variable is it's data type.

### Short defination of Data Types:
Data Types are cotegories of of data that dertimines the type of value a variable can hold, such as numbers, texts, or boolean values.

### Long defination of Data Types:
Data Types are classification of data that define the characteristics, formats, and set of values that a varible, constant, or expression can hold, including numeric, textual, boolean, data, time, and other types, which influence that how the data is stored, processed, and intracted with in a programming language.
### Data Types in python:
- String 
- Integer
- Float
- Boolean
- List
- Tuple
- Set
- Dictonary
- None
- Complex

### Creating string in Python:
```python
name = "Adi"
print(name)
print(type(name))
```
#### Output
```bash
Adi
<class 'str'>
```
### Creating Integer in Python:
```python
age = 20
print(age)
print(type(age))
```
#### Output
```bash
20
<class 'int'>
```
### Creating Float in Python:
```python
height = 5.8
print(height)
print(type(height))
```
#### Output
```bash
5.8
<class 'float'>
```
### Creating Boolean in Python:
```python
isMale = True
print(isMale)
print(type(isMale))
```
#### Output
```bash
True
<class 'bool'>
```
### Creating List in Python:
```python
fruits = ["Apple", "Banana", "Mango", 135, 5.8, True]
print(fruits)
print(type(fruits))
```
#### Output
```bash
['Apple', 'Banana', 'Mango', 135, 5.8, True]
<class 'list'>
```
### Creating Tuples in Python:
```python
colors = ("Red", "Green", "Blue", 135, 5.8, True)
#You can avoid parenthesis in tuples
print(colors)
print(type(colors))
```
#### Output
```bash
('Red', 'Green', 'Blue', 135, 5.8, True)
<class 'tuple'>
```
### Creating Sets in Python:
```python
fruits = {"Apple", "Banana", "Mango", 135, 5.8, True}
print(fruits)
print(type(fruits))
```
#### Output
```bash
{'name': 'Adi', 'age': 20, 'height': 5.8, 'isMale': True}
<class 'set'>
```
### Creating Dictonary in Python:
```python
person = {
    "name" : "Adi",
    "age" : 20,
    "height" : 5.8,
    "isMale" : True
}
print(person)
print(type(person))
```
#### Output
```bash
{'name': 'Adi', 'age': 20, 'height': 5.8, 'isMale': True}
<class 'dict'>
```
### Defining None in Python:
```python
data = None
print(data)
print(type(data))
```
#### Output
```bash
None
<class 'NoneType'>
```
### Creating Complex number in Python:
```python
comp = 5 + 3j
print(comp)
print(type(comp))
```
#### Output
```bash
(5+3j)
<class 'complex'>
```

#### We will see this all Types in detail in other chapters.

#### For study in detail cheack out this video: 

## Thanks for your ataintion.