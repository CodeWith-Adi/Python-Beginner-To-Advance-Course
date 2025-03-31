# Using curly braces
# set1 = {1, 2, 5, 4, 3}

# Using set() constructor
# set2 = set([1, 2, 3, 4, 5])
# set3 = set("Hello")  # Creates a set of unique characters: {'H', 'e', 'l', 'o'}

# print(set1)
# print(set2)
# print(set3)

# my_set = {"apple", 2, True, "banana", 1, False}
# print(my_set)

# numbers = {1, 2, 3, 4, 5}

# # Adding elements - Adds a single element to the set
# numbers.add(6)
# print(numbers)

# # Removing elements - Removes specified element, raises KeyError if not found
# numbers.remove(1)
# print(numbers)

# # Removing all elements - Removes all elements from the set
# numbers.clear()  # Removes all elements from the set
# print(numbers) 

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (|) - Combines elements from both sets, removing duplicates
union_set = set1 | set2
print(union_set)
# Result: {1, 2, 3, 4, 5}

# Intersection (&) - Keeps only elements present in both sets
intersection_set = set1 & set2
print(intersection_set)
# Result: {3}

# Difference (-) - Keeps elements from first set that are not in second set
difference_set = set1 - set2
print(difference_set)
# Result: {1, 2}