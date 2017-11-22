def my_func(a: int, b: str, c: float) -> int:
    print(a, b, c)
    return a


def main():
    name: str = 3.4
    my_func(1, 2, 3.4)


if __name__ == '__main__':
    main()