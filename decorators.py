""" Let's create a decorator that validates the inputs of a function before execution. This is useful in scenarios

where you want to ensure that the inputs meet certain criteria before proceeding with the function logic.

Example: A decorator for input validation
We’ll create a decorator that validates the types and values of the arguments before the function executes.

Specifically, we'll:
1. Ensure that the inputs are of the correct data type.

2. Raise an error if the input does not meet certain conditions.

Step-by-Step Example:

Decorator that validates input types: We’ll make sure that arguments passed to a function are of the expected type
(e.g., ensuring a list is passed if expected).

Validate specific conditions: Additionally, we can add more logic, like ensuring the values are not negative

if that is a requirement.

"""
# Function to validate the data type of the input

def validate_inputs(expected_types):
    def decorater(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, expected_types):
                # Validate the types of positional arguments
                if not isinstance(arg, expected_type):
                    raise ValueError(f"Invalid type: Expected {expected_type} but got {type(arg)} for argument {arg}")

                # Additional validation for specific cases (example: no negative numbers)
                for arg in args:
                    if isinstance(arg, (int, float)) and arg < 0:
                        raise ValueError(f"Invalid value: Negative numbers are not allowed (got {arg})")

                # If validation passes, call the original function
                return func(*args, **kwargs)
        return wrapper
    return decorater

# Function to process data
@validate_inputs((list, int))
def process_items(items, multiplier):
    print(f"Processing {len(items)} items with multiplier {multiplier}")
    return [item * multiplier for item in items]

items = [1,2,3,4,5]
multiplier = 2
result = process_items(items, multiplier)

print(f"Input is {items} and output is {result}")
