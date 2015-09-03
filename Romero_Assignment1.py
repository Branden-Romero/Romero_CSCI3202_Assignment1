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

	def delete(self,value):
		if value in self.keys:
			self.delete_helper(value,self.root)
		else:
			print("Node not found.")

	def delete_helper(self,value,node):
		if node.left and node.left.key == value:
			if node.left.key == value and (node.left.left == None and node.left.right == None):
				node.left = None
			else:
				print("Node not deleted, has children")
		elif node.right and node.right.key == value:
			if node.right.key == value and (node.right.left == None and node.right.right == None):
				node.right = None
			else:
				print("Node not deleted, has children")
		else:
			if node.left:
				self.delete_helper(value,node.left)
			if node.right:
				self.delete_helper(value,node.right)
					
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
			
class Graph:
	def __init__(self):
		self.graph = dict()
	def addVertex(self,value):
		if self.graph.has_key(value):
			print("Vertex already exists.")
		else:
			self.graph[value] = []
	
	def addEdge(self,value1,value2):
		if self.graph.has_key(value1) and self.graph.has_key(value2):
			if value2 in self.graph[value1] and value1 in self.graph[value2]:
				pass
			else:
				self.graph[value1].append(value2)
				self.graph[value2].append(value1)
		
		else:
			print("One or more vertices not found.")

	def findVertex(self,value):
		if self.graph.has_key(value):
			print(self.graph[value])
		else:
			print("Vertex does not exist.")
def main():
	### 5.a Testing the queue ###
	
	#Constructing a FIFO Queue
	print("Queue Test:")
	queue = Queue.Queue()
	
	### 5.a.i. ###
	#Generating 10 values and storing them in a queue
	for i in range(0,10):
		queue.put(10**i)
	
	#Dequeuing the values and printing them
	while queue.empty() != True:
		print(queue.get())

	### 5.b Testing the stack ###
	print("Stack Test:")
	
	#Create an instance of a stack
	stack = Stack()
	
	## 5.b.i. ###
	#Generating 10 values and storing them in a queue
	for i in range(0,10):
		stack.push(10**i)

	#Popping the stack and printing the value
	while stack.checkSize() != 0:
		print(stack.pop())

	### 5.c Testing the tree ###
	print("Binary Tree Test:")

	#Create an instance of a binary tree
	tree = BinaryTree()
	
	## 5.c.i ##
	#Adding 10 value to the tree
	tree.add(10,1)
	tree.add(12,10)
	tree.add(11,10)
	tree.add(4,11)
	tree.add(3,12)
	tree.add(8,3)
	tree.add(14,4)
	tree.add(1,14)
	tree.add(7,14)
	tree.add(16,8)
	
	#Attempting to add a value to a parent with two children
	tree.add(99,10)

	#Attempting to add a value to a parent that does not exist
	tree.add(999,100)
	
	## 5.c.ii. ##
	#Printing tree
	tree.print_tree()

	## 5.c.iii ##
	#Deleting two nodes
	tree.delete(16)
	tree.delete(1)

	#Attempting to delete a node that has a child
	tree.delete(4)

	#Attempting to delete a node that does not exist
	tree.delete(999)

	## 5.c.iv. ##
	#Printing tree
	tree.print_tree()

	### 5.d Testing the graph ###
	print("Graph test:")

	#Creating an instance of a graph
	graph = Graph()
	
	## 5.d.i. ##
	#Adding 10 values to the graph
	for i in range(0,10):
		graph.addVertex(i)
	
	## 5.d.ii. ##
	#Adding at most 40 edges to the graph
	for i in range(0,40):
		value1 = random.randint(0,9)
		value2 = random.randint(0,9)
		graph.addEdge(value1,value2)
	
	## 5.d.iii. ##
	#Finding 5 vertices in the graph
	for i in range(1,6):
		graph.findVertex(i)	
	

if __name__== "__main__": main()
