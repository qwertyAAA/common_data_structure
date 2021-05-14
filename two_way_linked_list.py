from collections import deque
from typing import Any, Iterable, Optional


class Node(object):
    def __init__(self, prev_node=None, next_node=None, data=None):
        self.prev: Node = prev_node
        self.data: Any = data
        self.next: Node = next_node

    def __del__(self):
        """
        delete current node, and set the corresponding link structure
        :return: None
        """
        try:
            self.prev.next = self.next
        except AttributeError:
            pass
        try:
            self.next.prev = self.prev
        except AttributeError:
            pass
        del self

    def __str__(self):
        return str(self.data)


class TwoWayLinkedList(object):
    def __init__(self, list_data: Iterable):
        """
        create and link Nodes in list_data
        :param list_data: a Iterable composed of data
        """
        dq = deque(list_data)
        self.head = Node(data=dq.popleft())
        current_node = self.head
        self._current_node = self.head
        while dq:
            current_node.next = Node(prev_node=current_node, data=dq.popleft())
            current_node = current_node.next
            if not dq:
                self.tail = current_node

    def __iter__(self):
        return self

    def __next__(self):
        try:
            ret = self._current_node
            self._current_node = self._current_node.next
            return ret
        except AttributeError:
            self._current_node = self.head
            raise StopIteration

    def __len__(self):
        current_node = self.head
        length = 0
        while current_node.next:
            length += 1
            current_node = current_node.next
        return length

    def pop(self) -> Node:
        """
        pop a Node from list, right side first
        :return: Node
        """
        ret = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return ret

    def popleft(self) -> Node:
        """
        pop a Node from list, left side first
        :return: Node
        """
        ret = self.head
        self.head.next.prev = None
        self.head = self.head.next
        return ret

    def append(self, data: Any) -> None:
        """
        append a Node to list, right side first
        :param data: any data
        :return: None
        """
        node = Node(prev_node=self.tail, data=data)
        self.tail = node

    def append_left(self, data=Any):
        """
        append a Node to list, left side first
        :param data: any data
        :return: None
        """
        node = Node(data=data, next_node=self.head)
        self.head = node

    def extend(self, iterable: Iterable):
        """
        extend a Node Iterable to list, right side first
        :param iterable: an Iterable composed of any data
        :return: None
        """
        for data in iterable:
            node = Node(data=data, next_node=self.tail)
            self.tail = node

    def extent_left(self, iterable: Iterable):
        """
        append a Node to list, left side first
        :param iterable: an Iterable composed of any data
        :return: None
        """
        for data in iterable:
            node = Node(data=data, prev_node=self.head)
            self.head = node

    def insert(self, data: Any, index: Optional[int] = None, prev_node: Optional[Node] = None,
               next_node: Optional[Node] = None) -> Node:
        """
        insert a Node to list, need a positioning of Node in list
        the new node is inserted to the right of the node to which it is anchored
        :param data: any data
        :param index: index of Node positioning, like the index of common ist
        :param prev_node: the previous Node of the Node to be located
        :param next_node: the next Node of the Node to be located
        index, prev_node, next_node at least one is needed
        the priority of the above three parameters is index first, then prev_node, the last is next_node
        :return: inserted Node
        """
        if index:
            current_node = self.head
            for _ in range(index + 1):
                current_node = current_node.next
        elif prev_node:
            current_node = prev_node.next
        elif next_node:
            current_node = next_node.prev
        else:
            raise KeyError("please pass an index on insert method")
        prev_node = current_node
        next_node = current_node.next
        node = Node(prev_node=prev_node, data=data, next_node=next_node)
        return node

    def reverse(self) -> None:
        """
        reverse the whole list
        :return: None
        """
        current_node = self.head
        self.tail = self.head
        while current_node.next:
            current_node.prev, current_node.next = current_node.next, current_node.prev
