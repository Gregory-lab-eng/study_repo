"""A program that implements a single-linked list 
with methods for adding, removing, and searching elements."""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next
        if current:
            previous.next = current.next



    def find(self, key):
        current = self.head
        while current.value != key and current.next:
            current = current.next
        if current.value != key:
            return False
        else:
            return True


    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')
