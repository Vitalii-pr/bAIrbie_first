class Node:  # No change needed in the Node class
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:  # More concise base case handling
        return head  

    current = head
    while current.next:  # Implicitly checks for None
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head 
