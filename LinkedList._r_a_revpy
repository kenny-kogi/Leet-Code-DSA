# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




"""
Search a Linkded List in Python
"""


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
    
    """
    To print the results when we call the print(a_list)
    """
    def __str__(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next
            
    """ 
    Searching a linkded List
    """
    def search(self, target):
        current = self.head
        while current.next != None:
            if current.data == target:
                return True
            else:
                current = current.next
            return False
        
    """
    removing a node in a linked list
    """
    def remove(self, target):
        if self.head == target:
            self.next = self.next.next
        current = self.head 
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next
            
    """
    
    a b c
    
    next = b
    previos = b
    reversing a linked list
    """
    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous 
            previous = current
            current = next
        self.head = previous
            
a_list = LinkedList()
a_list.append("keeny")
a_list.append("eddy")
a_list.append("mike")
a_list.append("iraki")
print(a_list)
