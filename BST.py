# Author: Ewan GRIGNOUX LEVERT
# Date: 29/01/2021
from random import shuffle
 
class BST:# Binary Search Tree
    def __init__(self, value):
        self.label = value
        self.left_child = None
        self.right_child = None
    
    def search(self, value):
        """
        This method searches for a value in the BST.
        """
        if self.label == value:
            return True
        
        elif value < self.label:
            if self.left_child is None:
               return False
            else:
                return self.left_child.search(value)
        
        elif value > self.label:
            if self.right_child is None:
               return False
            else:
                return self.right_child.search(value)
    
    def insert(self, value):
        """
        This method inserts a value on BST.
        """
        if self.label == value :
            return False
        
        if value < self.label:
            if self.left_child == None:
                self.left_child = BST(value)
            else:
                self.left_child.insert(value)
        
        else:
            if self.right_child == None:
                self.right_child = BST(value)
            else:
                self.right_child.insert(value)

    def as_list(self):
        """
        This method returns a list with values of nodes in inorder path.
        """
        liste = []

        if self.left_child != None:
            liste += self.left_child.as_list()
        
        liste.append(self.label)

        if self.right_child != None:
            liste += self.right_child.as_list()
        
        return liste

    def remove(self, value):
        """
        This method removes a value in a BST.
        """
        if self.label == value:
            
            if (self.left_child == None) and (self.right_child == None):
                self.label = None
                return

            if self.right_child == None:
                self.label = self.left_child.label
                self.left_child = self.left_child.left_child
                self.right_child = self.left_child.right_child

            elif self.left_child != None:
                temp = self.right_child.left_child
                self.label = self.right_child.label
                self.right_child = self.right_child.right_child

                if temp != None:
                    self.left_child.merge(temp)
        
        elif value > self.label:
            self.right_child.remove(value)
        else:
            self.left_child.remove(value)

    def merge(self, tree):
        """
        This method needs a BST and self, and it merges tree in self.
        """
        if tree is None:
            return

        self.insert(tree.label)
        self.merge(tree.left_child)
        self.merge(tree.right_child)

    def insert_liste(self, tree):
        """
        This method needs a tree and insert its label in self.
        For this, it uses as_list().
        """
        liste = arbre.as_list()
        while len(liste) != 0:
            self.insert(liste[len(liste)//2])
            liste.remove(len(liste)//2)

    def jean_c_as_text(self, niveau=0):
        """
        This methods has name of France's Prime Minister, Jean Castex.
        It return a str which it represents tree.
        """
        text = f"{'  '*niveau}{self.label}\n"

        if self.left_child is not None:
            text += self.left_child.jean_c_as_text(niveau + 1)

        if self.right_child is not None:
            text += self.right_child.jean_c_as_text(niveau + 1)

        return text
    
    def __str__(self):
        return self.jean_c_as_text()


def Create_bst(liste):
    """
    This function takes a list and create a BST with its elements.
    """
    shuffle(liste)
    A = BST(liste[0])
    liste.remove(liste[0])
    for i in liste:
        A.insert(i)
    return A


A = Create_bst([9,12,7,8,15,-5,12.5,48.2,75,128,2,47,251690])
B = Create_bst([4,9,11])
A.merge(B)
print(A)
A.remove(9)
print(A)