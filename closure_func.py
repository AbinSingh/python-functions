# Example for closure
def outer_func(pinc_code):
    print(f"outer function scope {pinc_code}")
    def inner_func():
        print(f"outer function scope {pinc_code} is accessible under inner function")
    return inner_func

closure = outer_func("628215")
closure()

