
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

operation_function = operations[operation_selection]

answer = operation_function(n1=num1, n2=num2)

print(f"{num1} {operation_selection} {num2} = {answer}")