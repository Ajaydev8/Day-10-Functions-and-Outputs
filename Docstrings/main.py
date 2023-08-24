# Docstrings are basically a way for us to create little bits of documents as we're coding along in our
# functions or in our other blocks of code.

def format_name(f_name, l_name):
    # between these 3 quotation mark I can write something that i want the future developers to know about.
    """Takes a first name and last name and format it to return the title case version of the name. """
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"
    # This won't be printed since return is the end of the function.
    print("This should not be printed since the above code contains return function and we already returned a value.")


# if you'll hover over the format_name you'll see a text indicating what it actually does.
# That's what a Docstring is.
format_name()