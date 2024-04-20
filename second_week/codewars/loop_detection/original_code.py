def loop_size(node):
    slow = node
    fast = node
    
    while True:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow = node
    
            while slow != fast:
                slow = slow.next
                fast = fast.next
        
            loop_len = 1
            curr = slow.next
            while slow != curr:
                loop_len += 1
                curr = curr.next
            return loop_len
