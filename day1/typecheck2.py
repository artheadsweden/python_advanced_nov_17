from functools import wraps
from inspect import signature


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)

        bound_types = sig.bind(*ty_args, **ty_kwargs).arguments
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs).arguments
            for name, value in bound_values.items():
               if name in bound_types:
                   if not isinstance(value, bound_types[name]):
                       raise TypeError(f"Argument {name} is {type(value)}, expected {bound_types[name]}")
            return func(*args, **kwargs)
        return wrapper
    return decorate

def typecheck(func):
    if not __debug__:
        return func
    sig = signature(func)
    bound_types = sig.parameters

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_values = sig.bind(*args, **kwargs).arguments
        for name, value in bound_values.items():
            if not isinstance(value, bound_types[name].annotation):
                raise TypeError(f"Argument {name} is {type(value)}, expected {bound_types[name]}")
        if 'return' in func.__annotations__:
            return_value = func(*args, **kwargs)
            if not isinstance(return_value,func.__annotations__['return']):
                raise TypeError(f"Return value is {type(return_value)}, expected {func.__annotations__['return']}")
            else:
                return return_value
        else:
            return func(*args, **kwargs)
    return wrapper

@typecheck
def tryme(a: int, b: str, c: float) -> int:
    print(a, b, c)
    return b

def main():
    tryme(1, "hi", 4.5)


if __name__ == '__main__':
    main()