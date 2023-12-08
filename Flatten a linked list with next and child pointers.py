"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # If the head is null then return null
        if head is None:
            return None
        # Create a stack and push the head into it
        stack = []
        stack.append(head)
        # Create a dummy node
        dummy = Node(0,None,None,None)
        # Create a prev node and assign it to dummy
        prev = dummy
        # Iterate until the stack is empty
        while stack:
            # Pop the top element from the stack
            curr = stack.pop()
            # Assign the next of prev to curr
            prev.next = curr
            # Assign the prev of curr to prev
            curr.prev = prev
            # If the next of curr is not null then push it into the stack
            if curr.next is not None:
                stack.append(curr.next)
            # If the child of curr is not null then push it into the stack
            if curr.child is not None:
                stack.append(curr.child)
            # Assign the child of curr to null
            curr.child = None
            # Assign the prev to curr
            prev = curr
        # Assign the prev of dummy to null
        dummy.next.prev = None
        # Return the next of dummy
        return dummy.next

        