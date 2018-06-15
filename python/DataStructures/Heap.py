"""

Heap.py
Heap data strcuture implementation
Heap - balanced bnary tree where each child node is greater (or less than) parent. 
	- implementing MinHeap here
	- can be used for PiorityQueue

"""
class Heap:
	def __init__(self):
		self.heapList = [0] # the first element is a spaceholder and will remain unused to make indexing easier
		self.size = 0
	def insert(self, item):
		self.heapList.append(item)
		self.size += 1
		self.swim(self.size)
	def swap(self, i, j):
		tmp = self.heapList[i]
		self.heapList[i] = self.heapList[j]
		self.heapList[j] = tmp
	def swim(self, i):
		p = i // 2
		while i > 1 and self.heapList[p] > self.heapList[i]:
			self.swap(i,p)
			i = p
			p = i // 2
	def sink(self, i):
		while 2*i <= self.size:
			j = 2*i
			# select the smaller child
			if j < self.size and self.heapList[j] > self.heapList[j+1]:
				j = j + 1
			# swap if child is smaller than parent
			if self.heapList[j] < self.heapList[i]:
				self.swap(i,j)
			i = j
	def delMin(self):
		item = self.heapList[1]
		self.swap(1,self.size)
		self.heapList[self.size] = None
		self.size -= 1
		self.sink(1)
		return item

if __name__ == '__main__':
	H = Heap()

	items = [1,7,9,3,6,2,8, 13, 54, 5,17]
	for i in items:
		H.insert(i)

	m = H.delMin()
	ordered = []
	while m is not None:
		# print(m)
		ordered.append(m)
		m = H.delMin()

	print("Ordered list:")
	print(ordered)

