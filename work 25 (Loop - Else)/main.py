for i in range(5):
    print(i)
else:
    print("Loop completed")

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("While loop completed")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Hello")