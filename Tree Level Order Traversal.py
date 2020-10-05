class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
##Implementation of data structure queue
class Queue:
    def __init__(self):
        self.__rear=0
        self.__front=0
        self.__list=[]
        
    def enque(self,data):
        self.__list.append(data)
        self.__front+=1
    def deque(self):
        if self.__rear==self.__front:
            return "Queue is Empty : Can't DEQUE"
        self.__rear+=1
        
    def peek(self):
        if self.__rear==self.__front:
            return "Queue is Empty : Can't DEQUE"
        return self.__list[self.__rear]
    
    def print_queue(self):
        if self.__rear==self.__front:
            return "Queue is empty:"
        for i in range(self.__rear,self.__front):
            print(self.__list[i])
            
    def size(self):
        return (self.__front-self.__rear)
    
    def isEmpty(self):
        return True if self.__rear==self.__front else False
        
def levelOrder(root):
    q=Queue()
    q.enque(root)
    while q.size()!=0:
        curr=q.peek()
        if curr.left:
            q.enque(curr.left)
        if curr.right:
            q.enque(curr.right)
        print(curr.info,end=" ")
        q.deque()
        




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)