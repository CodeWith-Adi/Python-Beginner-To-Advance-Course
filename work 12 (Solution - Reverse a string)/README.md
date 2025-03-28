# Solution - Revrse a String

## Using Slicing :
Here's How :
```python
my_string = "Hello"
my_string = my_string[::-1]
print(my_string)
```

## Using lists
Here's How : 
```python
my_string = "Hello"
my_string = list(my_string)
my_string.reverse()
my_string = ''.join(my_string)
print(my_string)
```

## Using reversed() function
Here's How :
```python
my_string = "Hello"
my_string = ''.join(reversed(my_string))
print(my_string)
```

Watch this video for more information : https://youtu.be/Nwk4oWIJ_vY