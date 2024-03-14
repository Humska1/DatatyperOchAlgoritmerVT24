# -*- coding: utf-8 -*-

"""
Written by Lena Kallin Westin <kallin@cs.umu.se>. 
May be used in the course Datastrukturer och Algoritmer (Python) at Umeå University.
Usage exept those listed above requires permission by the author.
"""

import random
import time
import sys
import math
from TableAsArray import Table as ATable
from TableAsMTF import Table as MTFTable
from TableAsList import Table as LTable

def getTable(name):
    """Checks the name of the table type and creates a table of the type
       and returns it.
       
       Args:
           name - name of the table type to create
       
       Returns: 
	   A table of the given type    
    """
    if name == "TableAsArray":
        table = ATable()
    elif name == "TableAsList":
        table = LTable()
    else: 
        table = MTFTable()
    return table
    
def testIsempty(tableType):
    """Tests if isempty returns true directly after a table is created.
    
       Args:
           tableType - name of the table type to create and test
	   
    """    
    table = getTable(tableType)
    if not table.isempty():
        sys.exit("An newly created empty table is said to be nonempty.")
    print("Isempty returns true directly after a table is created. - OK")
	
def testInsertSingleElement(tableType):
    """Tests if isempty returns false directly after a table is created 
       and one element (key-value-pair) is inserted to it.
       
       Args:
           tableType - name of the table type to create and test
    """      
    table = getTable(tableType)
    table.insert("key1", "value1")
    if table.isempty():
        sys.exit("A table with one inserted element is seen as empty.")	
    print("Isempty false if one element is inserted to table. - OK")
    
def testLookupExistingKey(table, key, value):
    """Tests looking up the key key in a table table. Checks that lookup is
       returning true and the value value
       
       Args:
           table - the table to do the lookup in
	   key - the key to lookup
	   value - the expected value
    """
    (ok, returnValue) = table.lookup(key)
    if not ok:
        sys.exit("Looked up an existing key, table claims it does not exist.")
    if returnValue != value:
        msg = "Looked up a key but the value returned was wrong."
        msg = msg + " Expected: " + str(value) + " but got " + str(returnValue)    
        sys.exit(msg)        

def testLookupSingleElement(tableType):
    """Tests a table by creating it and inserting one key-value-pair. After 
       that it is checked that the returned values from a lookup are the ones 
       expected. First by looking up a non-existent key, then by looking up 
       an existent key.
       
       It is assumed that testInsertSingleValue has been run before calling 
       this test, i.e. that it has been tested that inserting one element 
       results in an nonempty table.
       
       Args:
           tableType - name of the table type to create and test
    """       
    table = getTable(tableType)
    table.insert("key1", "value1")  
    # Lookup a non-existent key
    (ok, value) = table.lookup("key2")
    if ok:
        sys.exit("Looked up non-existing key, table claims it does exist.")	
    print("Test of looking up non-existing key in a table with one element - OK")
    # Lookup a existent key
    testLookupExistingKey(table, "key1", "value1")
    print("Looking up existing key in a table with one element - OK")
    

def testInsertLookupDifferentKeys(tableType):	
    """Tests a table by creating it and inserting three key-value-pairs with 
       unique keys. After that, a lookup for all three keys are tested and 
       it is checked that the returned values are the ones expected.
       
       It is assumed that testInsertSingleValue and testLookupSingleValue
       has been run before calling this test, i.e. that it has been tested 
       that inserting one element results in an nonempty table and that 
       looking up an key-value-pairs is working with tablesize=1.
       
       Args:
           tableType - name of the table type to create and test
    """     
    table = getTable(tableType)
    table.insert("key1", "value1")  
    table.insert("key2", "value2")  
    table.insert("key3", "value3")  
    
    testLookupExistingKey(table, "key1", "value1")
    testLookupExistingKey(table, "key2", "value2")
    testLookupExistingKey(table, "key3", "value3")
    print("Looking up three existing keys-value pairs in a table with three elements - OK")
    
def testInsertLookupSameKeys(tableType):	
    """Tests a table by creating it and inserting three key-value-pairs with 
       the same keys. After that, a lookup for the key is tested and it is 
       checked that the returned value is the last one inserted to the table.
       
       It is assumed that testInsertSingleValue and testLookupSingleValue
       has been run before calling this test, i.e. that it has been tested 
       that inserting one element results in an nonempty table and that 
       looking up an key-value-pairs is working with tablesize=1.
       
       Args:
           tableType - name of the table type to create and test
    """     
    table = getTable(tableType)
    table.insert("key1", "value1")  
    table.insert("key1", "value2")  
    table.insert("key1", "value3")  
    
    testLookupExistingKey(table, "key1", "value3")   
    print("Looking up existing key and value after inserting the same key three times with different values - OK")

def testRemoveSingleElement(tableType):
    """Tests a table by creating it and inserting one key-value-pair. After
        that the element is removed and it is checked that the table is empty.
	
	It is assumed that testInsertSingleValue has been run before calling 
	this test, i.e. that it has been tested that inserting one element 
	results in an nonempty table.
	
       Args:
           tableType - name of the table type to create and test
	"""           
    table = getTable(tableType)
    table.insert("key1", "value1")  
    table.remove("key1")
    if not table.isempty():
        sys.exit("Removing the last element from a table does not result in an empty table.")
    print("Inserting one element and removing it, checking that the table gets empty - OK")
	
def testRemoveElementsDifferentKeys(tableType):
    """Tests a table by creating it and inserting three key-value-pairs. After
        that the elements is removed one at a time and it is checked that the 
	table is empty after the third element is removed.
	
	It is assumed that testInsertSingleValue and testRemoveSingleValue 
	have been run before calling this test, i.e. that it has been tested 
	that inserting one element results in an nonempty table and removing
	one element from a table with one element results in an empty table.
	
       Args:
           tableType - name of the table type to create and test
	"""           
    table = getTable(tableType)
    table.insert("key1", "value1")  
    table.insert("key2", "value3")  
    table.insert("key3", "value2")  	
    table.remove("key1")
    if table.isempty():
        sys.exit("Should be two elements left in the table but it says it is empty")	    
    table.remove("key2")
    if table.isempty():
        sys.exit("Should be one element left in the table but it says it is empty")	        
    table.remove("key3")
    if not table.isempty():
        sys.exit("Removing the last element from a table does not result in an empty table.")
    print("Inserting three elements and removing them, should end with empty table - OK")

def testRemoveElementsSameKeys(tableType):
    """Tests a table by creating it and inserting three key-value-pairs where 
        all three pairs have identical keys. After that the element is removed 
	and it is checked that the table is empty.
	
	It is assumed that testInsertSingleValue and testRemoveSingleValue 
	have been run before calling this test, i.e. that it has been tested 
	that inserting one element results in an nonempty table and removing
	one element from a table with one element results in an empty table.
	
       Args:
           tableType - name of the table type to create and test
	"""           
    table = getTable(tableType)
    table.insert("key1", "value1")  
    table.insert("key1", "value3")  
    table.insert("key1", "value2")  	

    table.remove("key1")
    
    if not table.isempty():
        sys.exit("Removing the last element from a table does not result in an empty table.")	
    print("Inserting three elements with the same key and removing the key, should end with empty table - OK")

def correctnessTest(tableType):
    """Tests a table by performing a set of tests. Program exits if any 
        error is found.
	
       Args:
           tableType - name of the table type to create and test
    """      
    testIsempty(tableType)
    testInsertSingleElement(tableType)
    testLookupSingleElement(tableType)
    testInsertLookupDifferentKeys(tableType)
    testInsertLookupSameKeys(tableType)
    testRemoveSingleElement(tableType)
    testRemoveElementsDifferentKeys(tableType)
    testRemoveElementsSameKeys(tableType)
    
def speedTest(tableType, noOfElements = 1000):
    """Tests the speed of a table using random numbers. First a number of 
       elements are inserted. Second a random lookup among the elements are 
       done followed by a skewed lookup (where a subset of the keys are 
       looked up more frequently). Finally all elements are removed.
       
       Args:
           tableType - name of the table type to create and test
	   noOfElements - the number of elements to work with, optional 
			  default value = 1000
    """      
    table = getTable(tableType)
    # Number of accesses to make to the table during lookup speed tests
    NROFACCESSES = noOfElements*2
    # The size of the random object space to generate
    RANDOMRANGE = noOfElements*3
    # Generates a sequence of noOfElements numbers from RANDOMRANGE for 
    # the keys and another sequence for the values
    keys = random.sample(range(RANDOMRANGE), noOfElements)
    values = random.sample(range(RANDOMRANGE), noOfElements)
    
    # Insert all items
    print("Insert " + str(noOfElements) + " items: ")
    start = time.process_time()
    for i in range(noOfElements):
	    table.insert(keys[i], values[i])
    end = time.process_time()
    print("%3.2f s." %(end-start))
    
    # Lookup randomly
    print("" + str(NROFACCESSES) + " random lookups: ")
    start = time.process_time()
    for i in range(NROFACCESSES):
        pos = random.randint(0, noOfElements-1)
        table.lookup(keys[pos]) 
    end = time.process_time()
    print("%3.2f s." %(end-start))
    
    # Lookup skewed to a certain range (in this case the middle third 
    # of the keys used
    startindex = math.trunc(math.floor(noOfElements/3))  
    stopindex = math.trunc(math.floor(noOfElements*2/3))  
    print("" + str(NROFACCESSES)+ " skewed lookups: ")
    start = time.process_time()
    for i in range(NROFACCESSES):
        pos = random.randint(startindex,stopindex)
        table.lookup(keys[pos])
    end = time.process_time()
    print("%3.2f s." %(end-start)) 

    # Lookup nonexistent keys
    print(str(NROFACCESSES) + " lookups with non-existent keys: ")
    # We know the keys have values in the area [0, RANDOMRANGE] so if we 
    # try to lookup keys in the area [RANDOMRANGE+1, RANDOMRANGE+NROFACCESSES+1]
    # they will not exist
    start = time.process_time()
    startindex = RANDOMRANGE+1
    for i in range(NROFACCESSES):
        table.lookup(startindex + i)
    end = time.process_time()
    print("%3.2f s." %(end-start))  
    
    # Remove all items, not in the same order as they were inserted
    print("Remove all items: ")
    #change the order of the keys
    random.shuffle(keys) 
    start = time.process_time()
    for i in range(noOfElements):
        table.remove(keys[i])
    end = time.process_time()
    print("%3.2f s." %(end-start))    

# Main program
if (len(sys.argv) > 1):
    correctnessTest(sys.argv[1])
    print("Correctnes tests completed. Now performing speed tests")
else:
    correctnessTest("TableAsArray")
    print("Correctnes test of TableAsArray completed. Now performing speed tests")
    speedTest("TableAsArray", 1000)
    input("TableAsArray tes ts completed, press enter to continue!")
    
    correctnessTest("TableAsList")
    print("Correctnes test of TableAsList completed. Now performing speed tests")
    speedTest("TableAsList", 5000)
    input("TableAsList tests completed, press enter to continue!")
    
    correctnessTest("TableAsMTF")
    print("Correctnes test of TableAsMTF completed. Now performing speed tests")
    speedTest("TableAsMTF", 5000)
    input("TableAsMTF tests completed, press enter to continue!")

