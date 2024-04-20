class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    current = head

    if head is None:
        return head

    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
