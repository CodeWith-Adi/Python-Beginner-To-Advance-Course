# CLI Calculator
while True:
    question = input("Enter an expression: ")
    if question == "exit":
        print("Thanks for using me.....😇")
        break
    else:
        solution = eval(question)
        print(f"The solution of {question} is : {solution}")