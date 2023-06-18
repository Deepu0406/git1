# Implementing OO Single Linked List



class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None # By default the node object next is - none 
        # it helps in making the current node as the last node 

class LinkedList(object):
    def __init__(self, head=None):  # identifies the first node -- anchor 
        self.head = head 

    def append(self,new_node):
        current = self.head 
        if current:
            while current.next: # Identify the last node 
                current = current.next
            current.next = new_node # Identify the new node as the last node 
        else:
            self.head = new_node # the first node    

    def display(self):
        current = self.head 
        while current:
            print ("Value:", current.value)
            current = current.next 


# driver code 
nodeObj = Node("Python")
nodeObj2 = Node("Simula")                             
nodeObj3 = Node("Dart")
nodeObj4 = Node("Haskell")
nodeObj5 = Node("F#")
nodeObj6 = Node("D")
nodeObj7 = Node("Groovy")

llObj = LinkedList(nodeObj)
llObj.append(nodeObj2)
llObj.append(nodeObj3)
llObj.append(nodeObj4)
llObj.append(nodeObj5)

llObj.display()
llObj.append(nodeObj6)
llObj.append(nodeObj7)
print("\n New nodes appended")
llObj.display()