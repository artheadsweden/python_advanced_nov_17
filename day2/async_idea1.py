from itertools import islice

def fib():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a + b

def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("Not found")


def main():
    fibs = list(islice(fib(), 10))
    print(fibs)

    result = search(fib(), lambda x: len(str(x)) >= 6)

    print(result)


if __name__ == '__main__':
    main()