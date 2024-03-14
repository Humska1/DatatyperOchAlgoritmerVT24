# -*- coding: latin-1 -*-

#Written by Johan Eliasson <johane@cs.umu.se> based on an original by
#Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Umeå University.
#Usage exept those listed above requires permission by the author.   

"""
Datatypen ordnad riktad graf med möjlighet till att ha vikter på noderna.
Datatypen följer till stora delar med undantag för 3 funktioner för att hantera 
vikter på kanterna definitionen av datatypen Graf på sidan 339 i
Lars-Erik Janlert, Torbjörn Wiberg Datatyper och algoritmer 2., [rev.] 
uppl.,Lund, Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7 

Variabler och funktioner som inleds med ett enkelt underscore "_" är privata
för klassen och ska inte användas av de som använder denna klass.

Denna klass implementerar en Graf.
"""
from Edge import Edge
from DirectedList import DirectedList
"""
    Datatypen Node som är en nod i en graf och som själv håller reda på sina grannar.
"""
"""
    Datatypen InternalEdge som är informationen om en nods granne och vikten 
    mellan dessa.
"""
class InternalEdge:
    def __init__(self, v, label=None):
        self._vertice = v
        self._label = label    
        
class Node:
    def __init__(self, v):
        """
            Syfte: Skapar en utökad nod-defintition från vertice v och en 
                   tom grannlista
            Pararmetrar: v - vertice i grafen 
        """         
        self._vertice = v
        self._noEdges = 0
        self._edges = []      
    
    def __str__(self):
        """
            Syfte: Skapar en strängrepresentation av Noden
        """
        return str(self._vertice)    

class DirectedGraph:
    def __init__(self, eqFcn):
        """
            Syfte: Skapar en tom graf
            Pararmetrar: eqFcn - en funktion som kan avgöra om två vertices är lika
            Returvärde: 
            Kommentarer: En tom graf
        """   
        self._nodes = [] # En lista av noder
        self._eqFcn = eqFcn
    
    def insertNode(self, vertice):
        """
            Syfte: Stoppar in en nod vertice i grafen.
            Pararmetrar: vertice - en nod
            Returvärde: 
            Kommentarer: 
        """     
        self._nodes.append(Node(vertice))
        
    def insertEdge(self, edge):
        """
            Syfte: Stoppar in en kant edge i grafen.
            Pararmetrar: edge - kanten som ska läggas till
            Returvärde: 
            Kommentarer: Förutsätter att noderna i edge finns i grafen. 
        """ 
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):                               
                node._edges.append(InternalEdge(v2)) 
                node._noEdges = node._noEdges + 1
        
    def isEmpty(self):
        """
            Syfte: Kollar om grafen är tom (utan noder)
            Pararmetrar: 
            Returvärde: True om grafen är tom, annars False
            Kommentarer: 
        """    
        return self._nodes == []
        
    def hasNoEdges(self):
        """
            Syfte: Kontrollerar om grafen saknar kanter
            Pararmetrar: 
            Returvärde: True om grafen saknar kanter, annars False
            Kommentarer: 
        """    
        for node in self._nodes:
            if node._edges != []:
                return False  #Vi fann en kant!
        return True
        
    def chooseNode(self):
        """
            Syfte: Väljer ut en av noderna i grafen och returnerar den
            Pararmetrar: 
            Returvärde: En nod i grafen.
            Kommentarer: 
        """  
        return self._nodes[0]._vertice
        
    def neighbours(self, vertice):
        """
            Syfte: Letar reda på grannarna till noden vertice
            Pararmetrar: vertice - en nod som man söker grannar till
            Returvärde: En lista med noderna som är grannar till noden vertice
            Kommentarer: 
        """   
        for node in self._nodes:
            if self._eqFcn(vertice, node._vertice):
                list = []
                for edge in node._edges:
                    list.append(edge._vertice)      
                return list                
        return []
    
    def deleteNode(self, vertice):
        """
            Syfte: Tar bort noden vertice ur grafen
            Pararmetrar: vertice - en nod som ska tas bort
            Returvärde: 
            Kommentarer: Förutsätter att noden vertice inte ingår i några kanter
        """     
        for node in self._nodes:
            if self._eqFcn(node._vertice, vertice):        
                self._nodes.remove(node)
                return

    def deleteEdge(self, edge):
        """
            Syfte: Tar bort kanten edge ur grafen
            Pararmetrar: edge - kanten som ska tas bort
            Returvärde: 
            Kommentarer: 
        """     
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):  
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2): 
                        node._edges.remove(edge)
                        node._noEdges = node._noEdges -1
                        return                 
                
    def hasEdgeLabel(self, edge):
        """
            Syfte: Kontrollerar om kanten har en vikt/ett värde
            Pararmetrar: edge - kanten som kan kontrollerar
            Returvärde: True om kanten har en vikt, annars False
            Kommentarer: Det förutsätts att kanten finns i grafen
        """    
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2):
                        return edge._label != None                 

        
    def setEdgeLabel(self, edge, label):
        """
            Syfte: Sätter vikten/värdet på kanten edge
            Pararmetrar: edge - kanten
                         label - etiketten
            Returvärde: 
            Kommentarer: Det förutsätts att kanten finns i grafen
        """  
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2):
                        edge._label = label   
        
    def inspectEdgeLabel(self, edge):
        """
            Syfte: Kontrollerar vikten/värdet på kanten edge
            Pararmetrar: edge - kanten som man kontrollerar
            Returvärde: Vikten/värdet på kanten edge
            Kommentarer: 
        """   
        (v1, v2) = edge.getVertices()
        for node in self._nodes:
            if self._eqFcn(node._vertice, v1):
                for edge in node._edges:
                    if self._eqFcn(edge._vertice, v2):
                        return edge._label              
    
    def __str__(self):
        """
            Syfte: Skapar en strängrepresentation av grafen
        """
        myStr = "Här kommer noderna och deras grannar!\n"
        for node in self._nodes:
            myStr = myStr + "\n" + str(node._vertice) + ", " 
            myStr = myStr + str(node._noEdges) + " grannar:\n"
            for edge in node._edges:
                myStr = myStr + str(edge._vertice) + ", " 
                if edge._label != None:
                    myStr = myStr + str(edge._label) + "\n"  
        myStr = myStr + "\n\n"              
        return myStr
