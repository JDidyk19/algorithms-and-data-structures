class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def push_front(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
        return self

    def pop_front(self):
        if self.is_empty():
            raise IndexError('list is empty')

        if self.head is self.tail:
            head_value = self.head
            self.head = self.tail = None
        else:
            head_value = self.head
            self.head = head_value.next
            self.head.prev = None
            head_value.next = None

        self.size -= 1
        return head_value.value

    def push_back(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1
        return self

    def pop_back(self):
        if self.is_empty():
            raise IndexError('list is empty')

        if self.head is self.tail:
            tail_value = self.tail
            self.head = self.tail = None
        else:
            tail_value = self.tail
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return tail_value.value

    def top_front(self):
        if self.head is not None:
            return self.head.value

        raise IndexError('list is empty')

    def top_back(self):
        if self.tail is not None:
            return self.tail.value

        raise IndexError('list is empty')

    def erase(self, value):
        if self.is_empty():
            raise IndexError('list is empty')

        current_node = self.head
        while current_node:
            if current_node.value == value:
                # if value is first element
                if current_node.prev is None:
                    self.head = self.head.next
                    self.head.prev = None
                # if value is last element
                elif current_node.next is None:
                    self.tail = self.tail.prev
                    self.tail.next = None
                # if element in the middle of the list
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev

                self.size -= 1

            current_node = current_node.next

        def find(self, value):
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    return True
                current_node = current_node.next

            return False
