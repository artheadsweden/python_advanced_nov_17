from pympler import asizeof

class NoSlots:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class WithSlots:
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


def main():
    no_slots = [NoSlots(str(n), n) for n in range(100000)]
    with_slots = [WithSlots(str(n), n) for n in range(100000)]

    size1 = round(asizeof.asizeof(no_slots)/1024/1024, 2)
    size2 = round(asizeof.asizeof(with_slots)/1024/1024, 2)

    print("No slots", size1, "mb")
    print("With slots", size2, "mb")

if __name__ == '__main__':
    main()