
# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Challange: create a dictionary where keys are each of the arithmatic symbols and the values are the name of the function.

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operation in operations:
    print(operation)

operation_selection = input("Which operation do you want to use?: ")
operation_function_1 = operations[operation_selection]
first_answer = operation_function_1(num1, num2)
print(f"{num1} {operation_selection} {num2} = {first_answer}")



operation_selection = input("Pick another symbol?: ")
num3 = int(input("What's the next number?: "))
operation_function_2 = operations[operation_selection]

#  Because we use the return function what I'm able to do is get hold of this operation function as a number here as you can see.

second_answer = operation_function_2(operation_function_1(num1, num2), num3)

print(f"{first_answer} {operation_selection} {num3} = {second_answer}")