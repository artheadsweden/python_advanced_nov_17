class A:
    def __init__(self, a, b, c, d):
        self.__dict__.update({k:v for k, v in locals().items() if k != 'self'})

def main():
    a = A('Alpha', 'Bravo', 'Charlie', 'Delta')
    print(a.a, a.b, a.c, a.d)

if __name__ == '__main__':
    main()