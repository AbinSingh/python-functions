"""
*args is a special syntax in Python used to allow a function to accept any number of positional arguments.

The *args syntax collects all the additional positional arguments passed to the function and stores them in a tuple.

"""

def func_args(*args):
    print(args)
    for arg in args:
        print(arg)

func_args([1,2,3], 100, "Example")

"""

**kwargs is a special syntax in Python used to allow a function to accept any number of keyword arguments. 

These keyword arguments are passed as key-value pairs, and **kwargs collects them into a dictionary inside the function.

"""

def func_kwargs(**kwargs):
    print(kwargs)

func_kwargs(name="abin", age="12", school="Amala Convent")

# function to experiment with both *args and **kwargs syntax
def func_args_kwargs(pin_code, *args, **kwargs):
    print(f"pincode is {pin_code}")
    for arg in args:
        print(f"this value:{arg} is fetched from args")
    print(f"this value:{kwargs} is fetched from kwargs")

func_args_kwargs(628215, [1,2,3], 100, "Example", name="abin", age="12", school="Amala Convent")