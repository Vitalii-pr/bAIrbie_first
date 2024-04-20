class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    seen = set()
    current = head
    prev = None

    while current:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next

    return head
