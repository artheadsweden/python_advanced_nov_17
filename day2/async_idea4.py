from collections import deque

from math import sqrt

import time


class Task:
    next_id =0

    def __init__(self, routine):
        self.id = Task.next_id
        Task.next_id += 1
        self.routine = routine


class Scheduler:

    def __init__(self):
        self.runnable_tasks = deque()
        self.completed_task_results = {}
        self.failed_task_errors = {}

    def add(self, routine):
        task = Task(routine)
        self.runnable_tasks.append(task)
        return task.id

    def run_to_completion(self):
        while len(self.runnable_tasks) != 0:
            task = self.runnable_tasks.popleft()
            print(f"Running task {task.id} ", end='')
            try:
                yielded = next(task.routine)
            except StopIteration as stopped:
                print(f"completed with result: {stopped.value}")
                self.completed_task_results[task.id] = stopped.value
            except Exception as e:
                print(f"failed with exception {e}")
                self.failed_task_errors[task.id] = e
            else:
                assert yielded is None
                print("now yielded")
                self.runnable_tasks.append(task)


def fib():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a + b


def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield

    raise ValueError("Not Found")

def async_print_matches(iterable, predicate):
    for item in iterable:
        #When is prime is async
        matches = yield from predicate(item)
        #if predicate(item):
        if matches:
            print(f"Found: {item}")
        #yield  - no longer needed

def async_sleep(interval_seconds):
    start = time.time()
    expiry = start + interval_seconds
    while True:
        yield
        now = time.time()
        if now >= expiry:
            break


def async_repetitive_message(message, interval_seconds):
    while True:
        print(message)
        yield from async_sleep(interval_seconds)

def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
        # yield
        yield from async_sleep(0)
    return True

def main():
    scheduler = Scheduler()
    scheduler.add(async_print_matches(fib(), lambda x: not any(x//i == x/i for i in range(x-1, 1, -1)))) # BLOCKING!!
    #scheduler.add(async_print_matches(fib(), async_is_prime))
    scheduler.add(async_repetitive_message("Mind the gap", 2))
    scheduler.run_to_completion()
if __name__ == '__main__':
    main()