class Node:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

class LinkedList:
    def __init__(self, headNode=None):
        self.headNode = headNode
    
    def setHead(self, node):
        self.headNode = node
    
    def traverse(self):
        nextLink = self.headNode

        while(nextLink != None):
            print(nextLink.head)
            nextLink = nextLink.tail

node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node4 = Node('node4')
node5 = Node('node5')

node1.tail = node2
node2.tail = node3
node3.tail = node4
node4.tail = node5

linkedList = LinkedList()

linkedList.setHead(node1)
linkedList.traverse()
