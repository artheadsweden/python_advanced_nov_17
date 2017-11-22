def outer(x):
    def inner(y):
        print(x, y)
    return inner

def main():
    f = outer(10)
    f(3)
    f2 = outer(20)
    f2(5)
    f(3)

    l = lambda x: lambda y: print(x,y)

    lf = l(15)
    lf(5)


if __name__ == '__main__':
    main()