class A:
    pass

class B:
    pass

# ======================

class Foo1(A, B):
    bar = 'baz'

    def spam(self):
        return 'ham ' + self.bar

# =======================

def spam(self):
    return 'ham ' + self.bar

body = {'bar': 'baz', 'spam': spam}

Foo2 = type('Foo2', (A, B), body)

# =====================

def main():
    f1 = Foo1()
    print(f1.spam())
    f2 = Foo2()
    print(f2.spam())


if __name__ == '__main__':
    main()