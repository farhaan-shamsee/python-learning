# a docstring is a string literal that is used to document a function, method, module, or class. 
# It is placed immediately after the definition and enclosed in triple quotes (""")

def add_numbers(a, b):
    """
    Add two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b


# The docstring for this function contains a brief description of what the function does, as well as a description of its parameters and return value. 
# This information can be accessed using the built-in help() function or through documentation tools like Sphinx.