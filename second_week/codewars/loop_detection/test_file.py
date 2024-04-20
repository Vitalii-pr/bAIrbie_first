import time
import optimized
import original_code


TESTS = [1000, 100_000, 1_000_000, 10_000_000]


class Node:
    def __init__(self, n=None):
        self.next = n


def test():
    for i in range(len(TESTS)):

        first_node = Node()
        curr = first_node
        for _ in range(TESTS[i]):
            curr.next = Node()
            curr = curr.next

        curr.next = first_node

        print(f'Testing {TESTS[i]}')

        start_time = time.time()
        original_code.loop_size(first_node)
        print('Original code:', time.time() - start_time)

        start_time = time.time()
        optimized.loop_size(first_node)
        print('Optimized code:', time.time() - start_time)

        print('-----------')


if __name__ == '__main__':
    print('Testing')
    test()