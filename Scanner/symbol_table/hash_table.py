from symbol_table.linked_list import *

class HashTable:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.dict = {x: LinkedList() for x in range(1, self.capacity + 1)}
        self.size = 0

    # function for hashing the keys
    def __hash__(self, key):
        # make sure that the key is a string
        key = str(key)
        hsum = 0
        # loop through each character of the key
        for index, char in enumerate(key):
            # add to the sum index + length of the key ^ current char code
            hsum += (index + len(key)) ** ord(char)
            # keep the sum lower than the capacity
            hsum = hsum % (self.capacity + 1)
            # keep the hashing range between 1 and capacity
            if hsum == 0:
                hsum += 1
        return hsum

    # insert a new key, value pair in the hash table and returns the position
    def insert(self, key):
        self.size += 1
        # hash the key
        index = self.__hash__(key)
        linked_list_index = self.dict[index].insert(Node(key))
        return (index, linked_list_index)

    # search the value in the table, return a tuple (table position, linked list position)
    # return 0  if the value wasn't found
    def look_up(self, value):
        value = str(value)
        for key in self.dict.keys():
            if self.dict[key].search(value) != 0:
                return key, self.dict[key].search(value)
        return 0

    # returns the number of element form the table
    def get_size(self):
        return self.size

    # prints the table as a table
    def pretty_print(self):
        result = ''
        for key in self.dict.keys():
            result += (str(key) + "\t: " + self.dict[key].pretty_print() + "\n")
        return result



