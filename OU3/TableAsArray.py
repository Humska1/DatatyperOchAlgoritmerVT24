# Written by Vuk Dimovic <vudi0001@student.umu.se>
# Free to use, no license required
"""
    The purpose of this file is to create a Table that utilizes a custom Array structure.
"""
from Array import Array

class Table:

    def __init__(self, cap=20000):

        """
        Purpose: Creates a empty static table based on a custom Array structure.
        Comment: This corresponds to the function Empty.
        """

        self.array = Array((0,), (cap - 1,))  
        self.size = 0
        self.cap = cap

    def insert(self, key, value):

        """
        Purpose: Insert a key-value pair to the table.
        Parameters: key: The associated key to the value.
                    value: A unique value that correspons to the key.
        Comment: Duplicate keys are not used, the existing keys will have updated values. 
        """

        #Check if table is full
        if self.size >= self.cap: 
            raise Exception("Table is full")
        
        #Iterates over the array to find the key
        for i in range(self.size):
            if self.array.inspectValue((i,))[0] == key: 
                self.array.setValue((i,), (key, value)) 
                return
        self.array.setValue((self.size,), (key, value))  
        self.size += 1

    def isempty(self):

        """
        Purpose: Checks if the table is empty.
        Returns: Boolean True is table is empty, False otherwise.
        """

        return self.size == 0

    def lookup(self, key):

        """
        Purpose: Searches for a key corresponding to its associated value.
        Parameters: key: A unique key to search the Array with.
        Returns: A tuple containing a Boolean, and the element. If the key exists return True and the element,
        False and None if otherwise.
        """

        #Iterate over the array to find the key
        for i in range(self.size):
            if self.array.inspectValue((i,))[0] == key:  
                return True, self.array.inspectValue((i,))[1] 
        return False, None


    def remove(self, key):

        """
        Purpose: Removes a key-value pair from the table.
        Parameters: key: Unique key to search the Array with.
        Comment: If the key is found, the elements to the right of the key will be shifted left to fill the gap.
        """

        found = False
        #Iterates through the array to find the key
        for i in range(self.size):
            if self.array.inspectValue((i,))[0] == key:
                found = True
                break
        if found:
            #Shift elements to the left to fill the gap
            for j in range(i, self.size - 1):
                self.array.setValue((j,), self.array.inspectValue((j + 1,))) 
            self.size -= 1
            self.array.setValue((self.size,), None) 
        else:
            raise ValueError("Key not found")
