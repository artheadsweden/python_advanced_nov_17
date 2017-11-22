def s(x, y):
    return x + y

def d(x, y):
    return x - y

def p(x, y):
    return x * y

def q(x, y):
    return x / y


def main():
    calc = {
        'sum': s,
        'diff': d,
        'product': p,
        'quotient': q
    }

    print(calc['sum'](2,3))
    print(calc['diff'](2,3))
    print(calc['product'](2,3))
    print(calc['quotient'](2,3))

    for k, f in calc.items():
        print(k, "=", f(2,3))

    calc2 = {
        'sum': lambda x, y: x + y,
        'diff': lambda x, y: x - y,
        'product': lambda x, y: x * y,
        'quotient': lambda x, y: x / y
    }

    for k, f in calc2.items():
        print(k, "=", f(2,3))

if __name__ == '__main__':
    main()