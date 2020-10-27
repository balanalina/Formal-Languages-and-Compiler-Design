# class for a Node
class Node:
    def __init__(self, val=None):
        self.val = val  # holds the value of the node
        self.nextNode = None  # holds the next node


# implementation of a singly linked list
class LinkedList:
    def __init__(self, head=None):
        self.headNode = head
        self.size = 0

    # inserts a new node at the end of the list, returns the position on which it was inserted
    def insert(self, new_node):
        # make sure that the new node is not linked to other nodes
        new_node.nextNode = None
        self.size += 1
        if self.headNode is None:
            self.headNode = new_node
            return 1
        else:
            index = 1
            current_node = self.headNode
            while current_node.nextNode is not None:
                current_node = current_node.nextNode
                index += 1
            current_node.nextNode = new_node
            return index + 1

    # searches for a value in the list and returns its position ( starting from 1), returns 0 if the value wasn't found
    def search(self, token):
        index = 1
        current_node = self.headNode
        while current_node is not None:
            if current_node.val == token:
                return index
            else:
                current_node = current_node.nextNode
                index += 1
        return 0

    # returns true if the list is empty, false otherwise
    def is_empty(self):
        if self.headNode is None:
            return True
        return False

    # returns the number of nodes in the list
    def get_size(self):
        return self.size

    # returns the elements of the list as a string
    def pretty_print(self):
        current_node = self.headNode
        list_as_string = ''
        while current_node is not None:
            list_as_string = list_as_string + str(current_node.val) + " "
            current_node = current_node.nextNode
        return list_as_string


