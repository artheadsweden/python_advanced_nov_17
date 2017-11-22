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

@typeassert(int, str, float)
def tryme(a, b, c):
    print(a, b, c)

def main():
    tryme(1, "Hi", 3.4)


if __name__ == '__main__':
    main()