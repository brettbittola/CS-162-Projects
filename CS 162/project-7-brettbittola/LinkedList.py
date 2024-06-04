# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 11/13/2023
# Description: Linked List class with recursive add, remove, contains, insert and reverse methods.

class Node:
    """Represents a node in a linked list"""
    def __init__(self, data):
        """Initializes a node with data and a pointer pointing to the next node"""
        self.data = data
        self.next = None


class LinkedList:
    """A linked list implementation of the List ADT"""
    def __init__(self):
        """Initializes an empty linked list"""
        self._head = None

    def get_head(self):
        """Returns the head of the linked list"""
        return self._head

    def add(self, val, current=None):
        """Recursively adds a node containing val to the end of the linked list"""
        if current is None:
            current = self._head

        if self._head is None:
            self._head = Node(val)
        elif current.next is None:
            current.next = Node(val)
        else:
            self.add(val, current.next)

    def remove(self, val, previous=None, current=None):
        """Recursively removes the node containing val from the linked list"""
        if self._head is None:
            return

        if current is None:
            current = self._head

        if current.data == val:
            if previous is not None:
                previous.next = current.next
            else:
                self._head = current.next
            return
        else:
            if current.next is not None:
                previous = current
                current = current.next
                self.remove(val, previous, current)

    def contains(self, val, current=None):
        """Returns true if the linked list contains a given node"""
        if current is None:
            current = self._head

        if current.data == val:
            return True
        else:
            current = current.next
            if current is None:
                return False
            else:
                return self.contains(val, current)

    def insert(self, val, pos, current=None, previous=None):
        """Inserts a node into a linked list in a given position"""
        if current is None:
            current = self._head

        if self._head is None:
            self._head = Node(val)
            return
        elif current.next is None:
            current.next = Node(val)
            return
        elif pos == 0:
            temp = Node(val)
            temp.next = self._head
            self._head = temp
            return
        else:
            if pos > 0:
                pos -= 1
                if pos == 0:
                    temp = current.next
                    current.next = Node(val)
                    current.next.next = temp
                    return
                else:
                    self.insert(val, pos, current.next, current)

    def reverse(self, previous=None, current=None):
        """Reverses the order of nodes in a linked list"""
        if current is None:
            current = self._head

        if current is not None:
            following = current.next
            current.next = previous
            if following is None:
                self._head = current
                return self._head
        return self.reverse(current, following)

    def to_plain_list(self, current=None, num_list=None):
        """Converts linked to list to plain list of values"""
        if num_list is None:
            num_list = []

        if self._head is None:
            return

        if current is None:
            current = self._head

        if current is not None:
            num_list.append(current.data)
            if current.next is not None:
                current = current.next
                self.to_plain_list(current, num_list)
        return num_list
