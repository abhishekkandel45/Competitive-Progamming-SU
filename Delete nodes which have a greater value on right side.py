class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def compute(self, head):
        # Reverse the linked list
        head = self.reverse(head)

        # Initialize max_node
        max_node = head

        # Traverse the reversed list
        curr = head
        while curr and curr.next:
            if curr.next.data < max_node.data:
                # If next node is less than max_node, delete it
                curr.next = curr.next.next
            else:
                # Otherwise, update max_node and move to next node
                max_node = curr.next
                curr = curr.next

        # Reverse the list again to restore original order
        head = self.reverse(head)

        return head








# Driver Code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # append at the end of the list
    def append(self, new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = self.tail.next

    def getNode(self, value):
        curr_node = self.head
        while curr_node and curr_node.data != value:
            curr_node = curr_node.next
        if (curr_node.data==value):
            return curr_node
        else:
            return None

    def printList(self):
        if self.head is None:
            print ('')
            return
        curr_node = self.head
        while curr_node:
            print (curr_node.data, end=' ')
            curr_node = curr_node.next
        print ('')

if __name__ == '__main__':
    while t > 0:
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)

        result = Solution().compute(a.head)
        a.head = result
        a.printList()
        t -= 1

  