from itertools import islice

def fib():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a + b

def async_search(iterable, predicate):
    for item in iterable:
        print("testing value", item)
        if predicate(item):
            return item
        yield
    raise ValueError("Not found")


def main():
    fibs = list(islice(fib(), 10))
    # print(fibs)

    gen = async_search(fib(), lambda x: x >= 10)

    next(gen)
    print("I'm doing something")
    next(gen)
    next(gen)
    next(gen)
    print("I'm doing something else")
    next(gen)
    next(gen)
    next(gen)
    print("Finished?")
    next(gen)



if __name__ == '__main__':
    main()