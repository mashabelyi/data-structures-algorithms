"""
LinkedList.py

Singly-Linked List implementation, iterable.

"""
from timeit import Timer

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	
	def __init__(self):
		'''
			Initialize with head = None
		'''
		self.head = None
	
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
		else:
			oldhead = self.head
			self.head = Node(data, oldhead)

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
			return oldhead

	def insert_tail(self, data):
		'''
			Insert at tail
			O(n)
		'''
		if self.is_empty():
			self.insert_head(data)
		else:
			tmp = self.head
			while tmp.next is not None:
				tmp = tmp.next
			tmp.next = Node(data, None)
	
	def delete_tail(self):
		'''
			Delete at tail
			O(n)
		'''
		last = self.head
		secondlast = None
		while tmp.next is not None:
			secondlast = last
			last = last.next

		if secondlast is not None:
			secondlast.next = None
		else:
			self.head = None

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
	LL = LinkedList()
	for i in range(0,20):
		LL.insert_head(i)

if __name__ == "__main__":
    # LL = LinkedList()
    # for i in range(0,20):
    	# LL.insert_head(i)
    # print(LL)

    t = Timer("test()", "from __main__ import test")
    print(t.timeit())

    #Test iterable
    # for item in LL:
    	# print(item)
