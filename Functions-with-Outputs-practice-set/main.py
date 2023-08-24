def my_function():
    # result is an output function.
    return int(3 * 2)

# This function's output will be saved inside this variable output
output = my_function()

print(output)

# Functions with outputs exercise 1
# Creating a Function which will include the first name and last name as parameters.

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"
    # This won't be printed since return is the end of the function.
    print("This should not be printed since the above code contains return function and we already returned a value.")


full_name = format_name("ajay", "mishra")

# you can print like this or
print(full_name)

# you can also print like this
print(format_name("ajay", "mishra"))

# Another method that will ask the user.

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
