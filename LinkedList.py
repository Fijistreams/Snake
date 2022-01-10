from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        
        printnode = self.head

        while(printnode is not None):
            print(f'{printnode.data}')
            printnode = printnode.nextnode
        print('')

def addNode(self, data):

    tail = self.head
    while(tail.nextnode is not None):
        tail = tail.nextnode

    tail.nextnode = Node(data)








    
