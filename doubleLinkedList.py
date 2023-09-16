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
        lastLink = None
        
        while(currentLink != None):
            if (currentLink.tail):
                currentLink.tail.prev = currentLink
            lastLink = currentLink
            currentLink = currentLink.tail

        currentLink = lastLink
        while (currentLink != None):
            print(currentLink.head)
            currentLink = currentLink.prev
            
nodeNames = ['node2', 'node1', 'node4', 'node3', 'node5']
nodes = []
index = 0

# creates node objects and links them up depending on the above array.

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
#linkedList.bruteForceReverse()
