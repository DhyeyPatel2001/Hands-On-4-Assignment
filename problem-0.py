from functools import wraps

def log_function_call_stack(func):
    """Logs the function call with its arguments.

    Args:
        func: The function to be decorated.

    Returns:
        A decorated function that logs the call before execution.
    """
    @wraps(func)
    def log_func(*args):
        """Logs the function call and its arguments, then calls the original function.

        Args:
            *args: The arguments passed to the function.

        Returns:
            The return value of the original function.
        """
        print(f'call {func.__name__}({", ".join(map(repr, args))})')
        return func(*args)
    return log_func

@log_function_call_stack
def fibb(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fibb(n-1) + fibb(n-2)

# Call the Fibonacci function with 5 as input
x = fibb(5)

print("\nFibonacci of 5 is: ", x)

"""
Call stack output:
--------------
call fibb(5)
call fibb(4)
call fibb(3)
call fibb(2)
call fibb(1)
call fibb(0)
call fibb(1)
call fibb(2)
call fibb(1)
call fibb(0)
call fibb(3)
call fibb(2)
call fibb(1)
call fibb(0)
call fibb(1)



Restructured Output (Manually):
------------------------------
fibb(5)
├── fibb(4)
│   ├── fibb(3)
│   │   ├── fibb(2)
│   │   │   ├── fibb(1)
│   │   │   └── fibb(0)
│   │   └── fibb(1)
│   └── fibb(2)
│       ├── fibb(1)
│       └── fibb(0)
└── fibb(3)
    ├── fibb(2)
    │   ├── fibb(1)
    │   └── fibb(0)
    └── fibb(1)
"""