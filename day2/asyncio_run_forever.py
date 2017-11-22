import asyncio

loop = asyncio.get_event_loop()


async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()


def main():
    future = asyncio.Future()
    asyncio.ensure_future(slow_operation(future))
    future.add_done_callback(got_result)
    try:
        loop.run_forever()
    finally:
        loop.close()


if __name__ == '__main__':
    main()