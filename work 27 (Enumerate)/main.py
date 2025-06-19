students = ["Rohan", "Ravi", "Riya", "Rohit", "Ramesh", "Adi"]

# n = 1
# for i in students:
#     print(n, i)
#     n += 1

# Using enumerate to achieve the same result

for index, student in enumerate(students, start = 1): # (0, "Rohan")
    print(index, student)