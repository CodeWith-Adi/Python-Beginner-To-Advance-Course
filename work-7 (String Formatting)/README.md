# String Formatting
## What is String formatting ?
String formatting is the process of inserting values into a string template, replacing placeholders with actual values, to create dynamic strings.

## Ways of formatting a string...
There are many wats to format a string some of them are listed below :

### 1. Concatination
Concatination is the process of combining two or more strings into a single string. In python, we use the `+` opetrator to concatenate strings.

#### Example:

```python
name = "Adi"
role = "Programmer"
print("Hello I am " + name + ", and I am a " + role)

# Output : Hello I am Adi, and I am a Programmer.
```
### 2. String Multiplication
String multiplication is the process of repeting a string a specified number of times using the `*` operator.

#### Example:
```python
print("Hello, World! " * 2)

# Output : Hello, World! Hello, World! 
```

### 3. String formatting with %
"string formatting with %" is a method of inserting values into a string using the `%` operator and placeholders.

#### Example:
```python
name = "Adi"
age = 25
height = 5.5

print("Hello this is %s, I am %d years old, and my height is %f." %(name, age, height))

# Output: Hello this is Adi, I am 25 years old, and my height is 5.500000.
```

Placeholders:
- %s - Strings
- %d - Integer
- %f - float

### 4. String formatting with `format()` method:
#### Example:
```python
name = "Adi"
age = 28
print("My name is {} and I'm {} years old.".format(name, age))

# Output: My name is Adi and I'm 28 years old.
```

### 5. f-String
F-string is a method of string formatting in Python that uses the `f` prefix before a string to insert values directly into the string.

#### Example:
```python
name = "Adi"
age = 26

print(f"My name is {name} and I am {age} years old.")

# Output: My name is Adi and I am 26 years old.
```

### Watch this video for better understanding - https://youtu.be/1ugtiIdA1Ok

# Thanks for reading....