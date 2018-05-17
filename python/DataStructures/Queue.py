"""

Queue implementation (first-in-first-out) uing LinkedList

enqueue(key)	| O(1)
dequeue()		| O(1)
is_empty()		| O(1)

"""

class Node:
	def __init__(self, data, next=None):
		self.data  = data 
		self.next = next

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, data):
		if self.is_empty():
			self.head = Node(data)
			self.tail = self.head
		else:
			oldtail = self.tail
			self.tail = Node(data)
			oldtail.next = self.tail

	def dequeue(self):
		if self.is_empty():
			return None

		oldhead = self.head
		self.head = oldhead.next
		if self.is_empty():
			self.tail = None
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
	s = Queue()
	for i in range(0,20):
		s.enqueue(i)
	s.dequeue()
	s.dequeue()
	print(s)