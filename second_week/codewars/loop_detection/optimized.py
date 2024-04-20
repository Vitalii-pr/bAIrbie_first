def loop_size(node):
    slow, fast = node, node.next.next

    while fast != slow:
        if not fast or not fast.next:
            return 0  # No loop found
        slow = slow.next
        fast = fast.next.next

    loop_count = 1
    fast = fast.next
    while fast != slow:
        loop_count += 1
        fast = fast.next
    return loop_count

