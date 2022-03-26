class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def set_head(self, node):
        self._head = node

    def get_head(self):
        return self._head

    def set_tail(self, node):
        self._tail = node

    def get_tail(self):
        return self._tail

    def append(self, data):
        new_node = Node(data)
        if self._head is None:
            self.set_head(new_node)
            self.get_head().set_next(self._tail)
        elif self._head is not None and self._tail is None:
            self._head.set_next(new_node)
            self.set_tail(new_node)
        else:
            self._tail.set_next(new_node)
            self.set_tail(new_node)


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_next(self, node):
        self._next = node

    def get_next(self):
        return self._next
