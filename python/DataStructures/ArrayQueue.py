"""
ArrayQueue.py

Queue (FIFO) - Array Implementation
- fized size Queue
- keep a head and tail pointer and cycle both

enqueue(key)	| O(1)
dequeue()		| O(1)
is_empty()		| O(1)

"""

class ArrayQueue:
	def __init__(self, capacity):
		self.capacity = capacity + 1
		self.head = 0
		self.tail = 0
		"""
		There is no concept of fixed capacity array in Python,
		so we initialize a list with None values
		"""
		self.queue = [None] * self.capacity

	def is_empty(self):
		return self.head == self.tail

	def is_full(self):
		return self.increment(self.tail) == self.head

	def enqueue(self, data):
		if self.is_full():
			raise Exception("Queue is full.");
		self.queue[self.tail] = data
		self.tail = self.increment(self.tail)

	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty.");

		key = self.queue[self.head]
		self.queue[self.head] = None
		self.head = self.increment(self.head)
		return key

	def increment(self, pointer):
		if pointer + 1 < self.capacity:
			return pointer + 1
		else:
			return 0

	def decrement(self, pointer):
		if pointer > 0:
			return pointer - 1
		else:
			return self.capacity - 1

	def __str__(self):
		return str(self.queue)


if __name__ == "__main__":
	Q = ArrayQueue(7)
	for i in range(0,7):
		Q.enqueue(i)
	print(Q)

	print("dequeued {}".format(Q.dequeue()))
	print("dequeued {}".format(Q.dequeue()))
	print("dequeued {}".format(Q.dequeue()))

	print(Q)

	for i in range(8,11):
		print("enqueued {}".format(i))
		Q.enqueue(i)

	print(Q)