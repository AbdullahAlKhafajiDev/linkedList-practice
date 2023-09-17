#Double Linked List in Python
class Node:
    def __init__(self, head=None, tail=None, prev=None):
        self.prev = prev
        self.head = head
        self.tail = tail

class LinkedList:
    def __init__(self, headNode=None):
        self.headNode = headNode
    
    def setHead(self, node):
        self.headNode = node
    
    def traverse(self):
        currentLink = self.headNode

        while(currentLink != None):
            print(currentLink.head)
            currentLink = currentLink.tail

    def bruteForceReverse(self):
        currentLink = self.headNode
        currentLink.prev = None
        previousLink = None
        
        while(currentLink != None):
            if (currentLink.tail):
                currentLink.tail.prev = currentLink
            previousLink = currentLink
            currentLink = currentLink.tail

        currentLink = previousLink
        while (currentLink != None):
            print(currentLink.head)
            currentLink = currentLink.prev
            
# creates node objects and links them up depending on the below array.
nodeNames = ['node1', 'node2', 'node3', 'node4', 'node5']
nodes = []
index = 0

##########################################
while(index < len(nodeNames)):
    node = Node(nodeNames[index])
    if (nodes != []):
        nodes[index - 1].tail = node
    nodes.append(node)
    index += 1
##########################################

linkedList = LinkedList()

linkedList.setHead(nodes[0])
linkedList.traverse()
# print()
linkedList.bruteForceReverse()
