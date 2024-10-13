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