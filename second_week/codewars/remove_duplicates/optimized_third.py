def remove_duplicates(head):
  """
  Removes duplicates from a sorted linked list.

  Args:
    head: The head of the linked list.

  Returns:
    The head of the list with duplicates removed.
  """

  if head is None:
    return head

  current = head
  runner = head.next

  while runner is not None:
    if current.data != runner.data:
      current.next = runner
      current = current.next
    runner = runner.next

  current.next = None
  return head
