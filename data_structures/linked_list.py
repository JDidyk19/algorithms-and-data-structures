class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def is_empty(self):
        return self.head is None

    def push_front(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node

        return self

    def pop_front(self):
        # when list is empty
        if self.head is None:
            return None

        # when list has 1 item
        if self.tail is None:
            head_node = self.head.value
            self.head = None
            return head_node

        # when list has 2 items
        if self.head.next is self.tail:
            head_node = self.head.value
            self.head = self.tail
            self.head.next = None
            self.tail = None
            return head_node

        # when list has at least 3 items
        head_node = self.head.value
        self.head = self.head.next

        return head_node

    def push_back(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        return self

    def pop_back(self):
        # when list is empty
        if self.head is None:
            return None

        # when list has 1 item
        if self.head is self.tail:
            head_node = self.head.value
            self.head = None
            return head_node

        # when list has 2 items
        if self.head.next is self.tail:
            tail_node = self.tail.value
            self.head.next = None
            self.tail = None
            return tail_node

        # when list has at least 3 items
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next

        tail_node = current_node.next.value

        self.tail = current_node
        current_node.next = None

        return tail_node

    def top_front(self):
        if self.head is not None:
            return self.head.value

        return None

    def top_back(self):
        if self.tail is not None:
            return self.tail.value

        return None

    def erase(self, value):
        # when list is empty
        if self.head is None:
            return None

        deleted_node = None
        while self.head and self.head.value == value:
            deleted_node = self.head
            self.head = self.head.next

        current_node = self.head
        if current_node is not None:
            while current_node.next:
                if current_node.next.value == value:
                    deleted_node = current_node.next
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next

        # when value is tail
        if self.tail.value == value:
            self.tail = current_node
        return deleted_node

    def find(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
