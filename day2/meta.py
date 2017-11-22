class MyMeta(type):
    def __init__(cls, name, bases, dct):
        print("name =", name)
        print("bases =", bases)
        print("dct =", dct)
        super(MyMeta, cls).__init__(name, bases, dct)

class P(object, metaclass=MyMeta):
    pass

def main():
    p = P()


if __name__ == '__main__':
    main()