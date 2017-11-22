import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number +1):
        print(f"Task {name}: Compute factorial({f})")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial{number} = {f}")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    ))
    loop.close()

if __name__ == '__main__':
    main()