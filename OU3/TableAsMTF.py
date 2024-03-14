# Written by Vuk Dimovic <vudi0001@student.umu.se>
# Free to use, no license required
"""
    The purpose of this file is to create a Table that utilizes a custom Directed List structure with a
    unique Move-To-Front algorithm.

"""

from DirectedList import DirectedList
class Table:

    def __init__(self):
        
        """
            Purpose: Creates a empty table which utilizes a directed list
            Comment: This corresponds to the function Empty. 
        """	        
        self._table = DirectedList()
      
    def insert(self, key, obj):
        """
            Purpose: Insert a key-value pair to the table
            Parameters: key: A unique key corresponding to the value
                        obj: A specific value corresponding to the key
        """
        #Check if table is full
        if self.isempty():
            self._table.insert(self._table.first(), (key, obj))
        
        else:
            found = False
            pos = self._table.first()
    
            #Iterates through the table to find the key or reach the ned
            while (not found) and (not self._table.isEnd(pos)):
                (newKey, newObj) = self._table.inspect(pos)
                if newKey == key:
                    found = True
                    pos = self._table.remove(pos)
                    pos = self._table.insert(self._table.first(), (key, obj)) 
                pos = self._table.next(pos)
            if not found:
                self._table.insert(self._table.first(), (key, obj))
        
    def isempty(self):

        """
            Purpose: Checks if the table is empty.
            Returns: Boolean True if the table empty, False otherwise.
        """        
        return self._table.isempty()

    def lookup(self, key):

        """
            Purpose: Finds a key-value pair from the table.
            Parameters: key: The key corresponding to a specific value
            Returns: A tuple containing a Boolean, and the element. If the key exists return True and the element,
            False and None if otherwise.
        """

        pos = self._table.first()
        #Iterates through the table to find the key or reach the ned
        while not self._table.isEnd(pos):            
            (newKey, newObj) = self._table.inspect(pos)
            if newKey == key:
                self._table.remove(pos)
                self._table.insert(self._table.first(), (newKey, newObj))
                return (True, newObj)
            pos = self._table.next(pos)
        return (False, None)
        
    def remove(self, key):

        """
            Purpose: Removea key-value pair from the table
            Parameters: key: A unique key to search the Array with.
            Comment: No effect if the key doesn't exist.
        """

        if not self.isempty():
            found = False
            pos = self._table.first()
            
            #Iterates through the table to find the key or reach the ned
            while (not found) and (not self._table.isEnd(pos)):
                (newKey, newObj) = self._table.inspect(pos)
                if newKey == key:
                    found = True
                    pos = self._table.remove(pos)
                else:
                    pos = self._table.next(pos)   
