import random
import time
import original, optimized_first, optimized_second, optimized_third
from memory_profiler import memory_usage


TESTS = [10, 100, 1000, 10_000, 1_000_000]

functions = [(original.remove_duplicates, 'Original: '), (optimized_first.remove_duplicates, 'First: '),
             (optimized_second.remove_duplicates, 'Second: '), (optimized_third.remove_duplicates, 'Third: ')]


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def create_sorted_linked_list(lst: list) -> Node:
    head = Node(lst[0])
    curr = head
    for i in lst[1:]:
        curr.next = Node(i)
        curr = curr.next
    return head


def generate_rand_arr(n: int) -> list:
    return sorted([random.randint(0, 100) for x in range(n)])


def test() -> None:
    for _ in TESTS:

        head = create_sorted_linked_list(generate_rand_arr(_))
        print(f'Testing {_}')
        for i in functions:
            start = time.time()
            start_memory = memory_usage()[0]
            i[0](head)
            end_memory = memory_usage()[0]
            print(f'{i[1] }Time: {time.time() - start}, Memory usage: {end_memory - start_memory}')
        print('--------')


test()