from functools import wraps

def add_signs(pre_sign, post_sign):
    def decorate(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return pre_sign + f(*args, **kwargs) + post_sign
        return wrapper
    return decorate

@add_signs("!!!", "???")
def greeting(name):
    return "Hi " + name


def main():
    print(greeting.__name__)
    print(greeting("Emma"))

if __name__ == '__main__':
    main()