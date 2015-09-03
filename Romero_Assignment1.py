import Queue
import random

class Stack:
	def __init__(self):
		self.stack = []
	def push(self,value):
		self.stack.append(value)
	def pop(self):
		return self.stack.pop()

	def checkSize(self):
		return len(self.stack)

class Node:
	def __init__(self,key,parent):
		self.key = key
		self.left = None
		self.right = None
		self.parent = parent

class BinaryTree:
	def __init__(self):
		self.root = None
		self.keys = []
	
	def add(self,value,parentValue):
		if not self.root:
			self.root = Node(value,None)
			self.keys.append(value)

		else:
			if parentValue in self.keys:
				self.keys.append(value)
				self.add_helper(value,parentValue,self.root)
			else:
				print("Parent not found.")
	
	def add_helper(self,value,parentValue,node):
		if node.key == parentValue:
			if not node.left:
				node.left = Node(value,node.key)
			elif not node.right:
				node.right = Node(value,node.key)
			else:
				print("Parent has two children, node not added")
		else:
			if node.left:
				self.add_helper(value,parentValue,node.left)
			if node.right:
				self.add_helper(value,parentValue,node.right)
					
	def print_tree(self):
		if not self.root:
			print("Tree is empty.")
		
		else:
			self.print_helper(self.root)

	def print_helper(self,node):
		print(node.key)
		if node.left:
			self.print_helper(node.left)
		if node.right:
			self.print_helper(node.right)
			

				
	def delete(value):
		print('hi')

	def printTree():
		print('hi')

class Graph:
	def addVertex(value):
		print('hi')

	def addEdge(value1,value2):
		print('hi')

	def findVertex(value):
		print('hi')

def main():
	### 5.a Testing the queue ###
	
	#Constructing a FIFO Queue
	print("Queue Test:")
	queue = Queue.Queue()
	
	#Generating 10 random values and storing them in a queue
	for i in range(0,10):
		queue.put(random.randint(0,100))
	
	#Dequeuing the values and printing them
	while queue.empty() != True:
		print(queue.get())

	### 5.b Testing the stack ###
	print("Stack Test:")
	stack = Stack()
	
	for i in range(0,10):
		stack.push(random.randint(0,100))

	while stack.checkSize() != 0:
		print(stack.pop())

	print("Binary Tree Test:")
	tree = BinaryTree()
	tree.add(10,1)
	tree.add(12,10)
	tree.add(11,10)
	tree.add(4,11)
	tree.add(3,12)
	#tree.add(99,100)
	tree.print_tree()
	

if __name__== "__main__": main()
