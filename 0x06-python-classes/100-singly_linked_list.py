#!/usr/bin/python3
"""Node class defined."""


class Node:
    """This is a Node."""

    def __init__(self, data, next_node=None):
        """Initialize a node.

        Args:
               data (int): integer to store in node.
               next_node (Node): node pointer
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Set/get node data attribute."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Set/get the next_node pointer."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""SinglyLinkedList class defined."""


class SinglyLinkedList:
    """This is a singlylinkedlist node."""

    def __init__(self):
        """Initialize the singlylinkedlist."""
        self.__head = None

    def sorted_insert(self, value):
        """Sorts and inserts nodes to the linked list.

        Args:
             value (int): integer to store in Node.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Print the SinglyLinkedList to stdout."""
        singll = []
        temp = self.__head
        while (temp is not None):
            singll.append(str(temp.data))
            temp = temp.next_node

        return ('\n'.join(singll))
