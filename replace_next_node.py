def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next

# node.val allows you to access the value that you're looking for
# node.next allows you to get the next item
