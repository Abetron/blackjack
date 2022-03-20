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

