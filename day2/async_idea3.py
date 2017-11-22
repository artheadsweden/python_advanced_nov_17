from collections import deque
from itertools import islice

class Task:
    next_id = 0

    def __init__(self, routine):
        self.id = Task.next_id
        Task.next_id += 1
        self.routine = routine

class Scheduler:
    def __init__(self):
        self.runnable_tasks = deque()
        self.completed_tasks = {}
        self.failed_tasks = {}

    def add(self, routine):
        task = Task(routine)
        self.runnable_tasks.append(task)
        return task.id

    def run_until_completion(self):
        while len(self.runnable_tasks) != 0:
            task = self.runnable_tasks.popleft()
            print(f"Running task {task.id} ", end='')
            try:
                yielded = next(task.routine)
            except StopIteration as stopped:
                print(f"completed with result: {stopped.value}")
                self.completed_tasks[task.id] = stopped.value
            except Exception as e:
                print(f"failed withexception {e}")
                self.failed_tasks[task.id] = e
            else:
                print(f"now yielded")
                self.runnable_tasks.append(task)


def fib():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a + b

def async_search(iterable, predicate):
    for item in iterable:
        print("testing value", item)
        if predicate(item):
            return item
        yield
    raise ValueError("Not found")


def main():
    scheduler = Scheduler()
    scheduler.add(async_search(fib(),lambda x: len(str(x)) >= 6))
    scheduler.add(async_search(fib(), lambda x: x >= 10))

    scheduler.run_until_completion()

    print("Task 0 ended with result", scheduler.completed_tasks.pop(0))
    print("Task 1 ended with result", scheduler.completed_tasks.pop(1))

if __name__ == '__main__':
    main()