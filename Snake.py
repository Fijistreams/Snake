from LinkedList import LinkedList


from LinkedList import LinkedList
from Node import Node
import copy

class Snake():
    def __init__(self):
        self.body = [
            [90,50],
            [80,50],
            [70,50]
        ] 

        self.TOUCHING = False
        self.linkedlist = LinkedList()
        headnode = Node([100,50])
        self.linkedlist.head = headnode
        node1 = Node([90,50])
        self.linkedlist.head.nextnode = node1
        node2 = Node([80,50])
        node1.nextnode = node2
        node3 = Node([70,50])
        node2.nextnode = node3

    def Move2(self, direction):
        if(direction == 'UP'):
            xylist = []

            templistnode = self.linkedlist.head

            while(templistnode.nextnode is not None):
                xylist.append(templistnode.data)
                templistnode = templistnode.nextnode

        xylist[0][1] = 10

        print(xylist)
        print(' ')
        self.linkedlist.printList()

    def Move(self, direction):
        oldvalue = self.linkedlist.head.data[:]

        tempnode = self.linkedlist.head
        tempv = None

        #head data for isTouching function
        headdata = self.linkedlist.head.data[:]
        
        while(tempnode.nextnode is not None):
            tempnode = tempnode.nextnode
            self.isTouching(headdata, tempnode.data)
            tempv = tempnode.data
            tempnode.data = oldvalue
            oldvalue = tempv

        if(direction == 'UP'):
            
            self.linkedlist.head.data[1] -= 10

        if(direction == 'DOWN'):
            
            self.linkedlist.head.data[1] += 10

        if(direction == 'LEFT'):
            
            self.linkedlist.head.data[0] -= 10
        self.linkedlist.printList()

        if(direction == 'RIGHT'):
            
            self.linkedlist.head.data[0] += 10

    def addSegment(self, direction):
        #self.linkedlist

        tail = self.linkedlist.head
        while(tail.nextnode is not None):
            tail = tail.nextnode

        newsegment = tail.data[:]
        if(direction == 'RIGHT'):
            newsegment[0] += 10

        if(direction =='LEFT'):
            newsegment[0] -= 10

        if(direction == 'UP'):
            newsegment[1] += 10
        
        if(direction == 'DOWN'):
            newsegment[1] -= 10
        
        tail.nextnode = Node(newsegment)

    def isTouching(self, head, segment):

        headx = head[0]
        heady = head[1]
        segmentx = segment[0]
        segmenty = segment[1]

        if(headx in range(segmentx-5, segmentx+5) and heady in range(segmenty-5, segmenty+5 )):
            self.TOUCHING = True





        


   
