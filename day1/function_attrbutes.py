
def function_object(n=0):
    private_value = n

    def func():
        print('private_value =', private_value)

    def increase_by(x):
        nonlocal private_value
        private_value += x

    def decrease_by(x):
        nonlocal private_value
        private_value -= x

    def get_value():
        return private_value

    def set_value(new_value):
        nonlocal private_value
        private_value = new_value

    func.increase_by = increase_by
    func.decrease_by = decrease_by
    func.get_value = get_value
    func.set_value = set_value

    return func



def main():
    f1 = function_object(20)
    f1()
    f1.increase_by(3)
    f1()
    f2 = function_object(99)
    f2()
    f1()


if __name__ == '__main__':
    main()