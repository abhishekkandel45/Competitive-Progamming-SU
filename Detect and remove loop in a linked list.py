class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        new=dict()
        s=head
        while s.next:
            if s.next not in new:
                new[s]=1
                s=s.next
            else:
                s.next=None
                return
                break
            return


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