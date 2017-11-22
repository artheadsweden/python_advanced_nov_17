
def outer(f):
    def inner(name):
        return ">>>" + f(name) + "<<<"
    return inner


def greeting(name):
    return "Hi " + name


def main():
    new_greeting = outer(greeting)
    print(new_greeting("Emma"))

if __name__ == '__main__':
    main()