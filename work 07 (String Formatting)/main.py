name = "Adi"
age = 28
height = 6.2

# 1. Concatination
print("My name is " + name + ", I am " + str(age) + " years old and I am " + str(height) + " feet tall.")

# 2. String Multiplication
print("Hello, World!" * 2)

# 3. String formatting with % operator
print("My name is %s, I am %d years old and I am %f feet tall." % (name, age, height))

# 4. String formatting using format method
print("My name is {}, I am {} years old and I am {} feet tall.".format(name, age, height))

# 5. f-String
print(f"My name is {name}, I am {age} years old and I am {height} feet tall.")