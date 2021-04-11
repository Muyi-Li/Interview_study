from collections import deque

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "This node has been inserted"

#space and time complexity O(logN)
 

#Traversal BST
def perOrderTraversal(rootNode): #root, left, right
    if not rootNode:
        return
    print(rootNode.data)
    perOrderTraversal(rootNode.leftChild)
    perOrderTraversal(rootNode.rightChild)

#time complexity O(n)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
#time and space O(n)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
#time and space O(n)

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = deque()
        customQueue.append(rootNode)
        while customQueue:
            root = customQueue.popleft()
            print(root.data)
            if root.leftChild:
                customQueue.append(root.leftChild)
            if root.rightChild:
                customQueue.append(root.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
       if rootNode.leftChild.data == nodeValue:
           print("This value is found")
       else:
           searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)
#time and space complexity O(logN)

def minValueNode(bstNode): #find a minimum value in the right subtree
    current = bstNode
    while current.leftChild: #the most left value of the right subtree is minimum\
        currnet = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):#(root parameter, value try to delete)
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:#value tries to delete is smaller than root
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:#no child or one child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

#space and time is O(log N)

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChlid = None
    rootNode.rightChild = None
    return "Successfully deleted"
#O(1) for both time and space

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
#perOrderTraversal(newBST)
#inOrderTraversal(newBST)
#postOrderTraversal(newBST)
#levelOrderTraversal(newBST)
#searchNode(newBST, 30)
#deleteNode(newBST, 100) 
#levelOrderTraversal(newBST) #use levelOrderTraversal to check if 100 has been deleted

print(deleteBST(newBST))
levelOrderTraversal(newBST)