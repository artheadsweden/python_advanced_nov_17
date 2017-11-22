from functools import partial


def power(base, pow):
    return base**pow


def square(n):
    return power(n, 2)


def cube(n):
    return power(n, 3)


def main():
    sq = partial(power, pow=2)
    cu = partial(power, pow=3)
    sq10 = partial(power, base=10, pow=2)

    print(sq(3))
    print(sq(4))
    print(cu(3))
    print(cu(4))
    print(sq10())

if __name__ == '__main__':
    main()