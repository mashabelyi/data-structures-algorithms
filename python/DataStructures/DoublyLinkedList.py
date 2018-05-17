"""
DoublyLinkedList.py

Doubly-Linked List implementation, iterable.

"""

from timeit import Timer

class Node:
	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class DoublyLinkedList:
	
	def __init__(self):
		'''
			Initialize with head = None
		'''
		self.head = None
		self.tail = None
	
	def __iter__(self):
		current = self.head
		while current is not None:
			yield current.data
			current = current.next
	
	def insert_head(self, data):
		'''
			Insert at head
			O(1)
		'''
		if self.head is None:
			self.head = Node(data, None)
			self.tail = self.head
		else:
			oldhead = self.head
			self.head = Node(data, oldhead)
			oldhead.prev = self.head

	def delete_head(self):
		'''
			Delete at head
			O(1)
		'''
		if self.head is None:
			return None
		else:
			oldhead = self.head
			self.head = self.head.next
			
			if self.head is None: 
				self.tail = None
			else:
				self.head.prev = None

			return oldhead

	def insert_tail(self, data):
		'''
			Insert at tail
			O(1)
		'''
		if self.is_empty():
			self.insert_head(data)
		else:
			oldtail = self.tail
			self.tail = Node(data, None, oldtail)
			oldtail.next = self.tail
	
	def delete_tail(self):
		'''
			Delete at tail
			O(1)
		'''
		last = self.tail
		self.tail = last.prev
		if self.tail is None:
			self.head = None
		else:
			self.tail.next = None

		return last

	def is_empty(self):
		return self.head == None

	def __str__(self):
		'''
		Prints the current list in the form of a Python list            
		'''
		current = self.head
		toPrint = []
		while current != None:
			toPrint.append(current.data)
			current = current.next
		return str(toPrint) 


def test():
	LL = DoublyLinkedList()
	for i in range(0,20):
		LL.insert_head(i)

if __name__ == "__main__":
    # LL = DoublyLinkedList()
    # for i in range(0,20):
    # 	LL.insert_tail(i)
    # print(LL)
    t = Timer("test()", "from __main__ import test")
    print(t.timeit())
