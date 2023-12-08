class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def zigzag(self, head_node):
        temp = head_node
        flag = True
        
        while temp and temp.next:
            if flag:
                if temp.data > temp.next.data:
                    num = temp.data
                    temp.data = temp.next.data
                    temp.next.data = num
            else:
                if temp.data < temp.next.data:
                    num = temp.data
                    temp.data = temp.next.data
                    temp.next.data = num
            
            temp = temp.next
            flag = not flag
        
        return head_node
