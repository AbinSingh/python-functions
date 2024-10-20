"""
Type Hinting and Annotations in Python

Type hinting is a feature introduced in Python 3.5 (via PEP 484) that allows you to indicate the expected types of
variables, function parameters, and return values. It is not enforced by Python at runtime
(Python is dynamically typed), but it helps developers and tools (like IDEs and linters) understand how your code
is supposed to work. This makes your code easier to read, maintain, and debug.

Annotations are the syntax used to provide these type hints in function signatures and variable declarations.

"""
## 1. Function Parameters and Return Types ##
def add_numbers(a: int, b: int) -> int:

    return a + b

print(add_numbers(10, 20))

# a: int means that the function expects a to be an integer.
# b: int means that the function expects b to be an integer.
# -> int means that the function is expected to return an integer.

## 2. Variable Type Hinting (Python 3.6+) ##

name: str = "Alice"
age: int = 25
is_student: bool = True

