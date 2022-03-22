# -*- coding: utf-8 -*-

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        current = self.head
        while current.next:
            current = current.next  
        current.next = Node(data)
        
    def __str__(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

            
a_list = LinkedList()
a_list.append("keeny")
a_list.append("eddy")
a_list.append("mike")
a_list.append("iraki")
print(a_list)
