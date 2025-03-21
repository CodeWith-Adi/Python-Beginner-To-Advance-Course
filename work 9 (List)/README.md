# What is List ?
A list is a data structure in Python that is mutable, or changeable, offered series of elements. Each element can be of any data type including strings, integers, floats, and other lists.


# Key Characteristics
1. Ordered: Lists maintain the order in which elements were added.
2. Mutable: Lists can be modified after creation.
3. Indexed: Each element is assigned an index `(starting from 0)`.
4. Dynamic: Lists can grow or shrink dynamically.

# Creating a List
You can create list by placing values beetween square brackets `[]`. Here is an example:

```python
my_list = ["Adi", 2, 8, 5.2, True, 3 + 5j, None, ["Apple", "Mango", "Banana"]]
```

# Indexing and Slicing
#### List elements are indexed starting from 0. 

### You can access elemets by their index:

```python
my_list = ["Adi", 2, 8, 5.2, True, 3 + 5j, None, ["Apple", "Mango", "Banana"]]
print(my_list[0])
# Output : "Adi"
```

### You can also slice list to get a subset of elements:

```python
my_list = ["Adi", 2, 8, 5.2, True, 3 + 5j, None, ["Apple", "Mango", "Banana"]]
print(my_list[1:5])
# Output : [2, 8, 5.2, True]
```

# List Methods
Lists are mutable so you can modify them after creation.

## 1. append(): 
Adds an element to the end of the list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  
# Output: [1, 2, 3, 4]
```



## 2. extend(): 

Adds multiple elements to the end of the list.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  
# Output: [1, 2, 3, 4, 5, 6]
```

## 3. insert(): 
Inserts an element at a specified position.

```python
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  
# Output: [1, 4, 2, 3]
```


## 4. remove(): 
Removes the first occurrence of an element.

```python
my_list = [1, 2, 3, 2, 3]
my_list.remove(2)
print(my_list)  
# Output: [1, 3, 2, 3]

```

## 5. pop(): 
Removes and returns an element at a specified position.


```python
my_list = [1, 2, 3]
print(my_list.pop(1))  # Output: 2
print(my_list)  # Output: [1, 3]
```


## 6. clear(): 
Removes all elements from the list.

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  
# Output: []
```

## 7. sort(): Sorts the list in-place.

```python
my_list = [3, 2, 1]
my_list.sort()
print(my_list)  
# Output: [1, 2, 3]
```

## 8. reverse(): Reverses the list in-place.

```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  
# Output: [3, 2, 1]
```

## 9. index(): 
Returns the index of the first occurrence of an element.

```python
my_list = [1, 2, 3]
print(my_list.index(2))  
# Output: 1
```

## 10. count(): 
Returns the number of occurrences of an element.

```python
my_list = [1, 2, 2, 3]
print(my_list.count(2))  
# Output: 2
```

Watch this video for better understanding: https://youtu.be/m-GtLWllHYE

Thanks for reading...💝💝 