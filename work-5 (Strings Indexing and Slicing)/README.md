# Strings in Python

## Defination:
A string is a sequence of characters such as letters, numbers and symbols, that are used to represent text. String is a fundamental data type in most of the programming language, including Python.

## Characterstics of Strings:
- Sequence of characters: A string is a collection of charachters, each with it's own position and index.
- Immutable : In python Strings are immutable, meaning that once a string defined, its contents cannot be modified.
- Orderd : The characters in a string have a specific order, and this order cannot be changed.
- Finite : A string has a finite length, meaning that it cannot contain an infinite numbers of characters.

## String Indexing and Slicing

### Indexing:
Indexing is a way to access individual charachters from an string.
<br>
`(The index always starts from 0)`
#### Example Code
```python
my_string = "Hello"
print(my_string[0]) # This will print "H" in console.
print(my_string[3]) # This will print "l" in console.
print(my_string[-1]) # This will print "o" in console.
```

### Slicing:
This method helps in extract a subset of characters.
#### Basic Slicing:
Extract a subset of charachters form a string using a syntax ->
<br>
`string[start : stop]`

#### Example Code
```python
my_string = "Hello"
print(my_string[1:3]) # This will print "el"
```

#### Slicing with Step:
Extracts characters at specified intervals, using the syntax ->
<br>
`string[start : stop : step]`

#### Example Code
```python
my_string = "Hello"
print(my_string[::2]) # This will print "Hlo"
```

#### Slicing with negarive indices:
Extract character from the end of a string, using the syntax ->
<br>
`string[-start : -stop]`

#### Example Code
```python
my_string = "Hello"
print(my_string[-4:-1]) # This will print "ell"
print(my_string[-2:]) # This will print "lo"
```

#### Slicing with omitted Start or Stops
Extracts characters from the beginning or to the end of a string, using the syntax ->
<br>
`string(: stop)` or `string(start :)`

#### Example Code
```python
my_string = "Hello"
print(my_string[1:]) # This will print "ello"
print(my_string[:-1]) # This will print "Hell"
```

## Watch this video for better understanding :-

# Thanks for Reading...