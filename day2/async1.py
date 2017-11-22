from time import sleep
import asyncio
loop = asyncio.get_event_loop()

def normal():
    print('Hi')
    sleep(3)
    print('Hi again')

@asyncio.coroutine
def coroutine():
    print('Hi')
    yield from asyncio.sleep(3)
    print('Hi again')

async def async_hello():
    print('Hi')
    await asyncio.sleep(3)
    print('Hi again')

def main():
    normal()
    loop.run_until_complete(coroutine())
    loop.run_until_complete(async_hello())

if __name__ == '__main__':
    main()