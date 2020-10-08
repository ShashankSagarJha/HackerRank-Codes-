class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        if self.root is None:
            self.root=Node(val)
        else:
            self._insert(self.root,val)
    
    def _insert(self,curr_node,data):
        if data<curr_node.info:
            if curr_node.left is None:
                curr_node.left=Node(data)
            else:
                self._insert(curr_node.left,data)
        elif data>curr_node.info:
            if curr_node.right is None:
                curr_node.right=Node(data)
            else:
                self._insert(curr_node.right,data)
        else:
            print("Can't Insert: {} already in the tree".format(data))

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)