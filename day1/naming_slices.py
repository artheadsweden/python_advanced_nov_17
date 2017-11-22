def main():
    data = "987234987234987329487239487235654656237329873298732948723987239874987"
    price = data[23:28]
    amount = data[31:33]

    print(price, amount)

    PRICE = slice(23, 28)
    AMOUNT = slice(31, 33)
    print(data[PRICE])
    print(data[AMOUNT])

if __name__ == '__main__':
    main()