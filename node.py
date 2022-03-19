class Node:
    def __init__(self, node_data) -> None:
        self.data = node_data,
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
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

    def search(self, target):
        current = self.head

        while current != None:
            if current.data == target:
                return True
            else:
                current = current.next
            return False
 
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
# print(a_list)
print(a_list.search("mike"))





