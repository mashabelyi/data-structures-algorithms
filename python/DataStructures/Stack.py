"""
Stack.py

Stack (last-in-first-out collection) - linked-list implementation 

Implements:
.push() 	| O(1)
.pop()		| O(1)
.is_empty()	| O(1)

"""
class Node:
	def __init__(self, data, next=None):
		self.data  = data 
		self.next = next

class Stack:

	def __init__(self):
		self.head = None

	def push(self, data):
		if self.is_empty():
			self.head = Node(data)
		else:
			oldhead = self.head
			self.head = Node(data, oldhead)

	def pop(self):
		oldhead = self.head
		self.head = self.head.next
		return oldhead

	def is_empty(self):
		return self.head == None

	def __str__(self):
		"""
		Prints the current list in the form of a Python list            
		"""
		current = self.head
		toPrint = []
		while current != None:
			toPrint.append(current.data)
			current = current.next
		return str(toPrint) 


if __name__ == "__main__":
	s = Stack()
	for i in range(0,20):
		s.push(i)
	s.pop()
	s.pop()
	print(s)
