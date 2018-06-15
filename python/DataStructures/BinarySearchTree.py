"""
BinarySearchTree.py

"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class BinarySearchTree:
	
	def __init__(self):
		self.root = None

	def get(self, value):
		"""
		Return node with given value
		"""
		return self.find(self.root, value)

	def find(self, N, value):
		if N is None: return None
		if N.value == value:
			return N
		elif N.value >= value:
			return self.find(N.left, value)
		elif N.value < value:
			return self.find(N.right, value)
		else: return None

	def insert(self, value):
		"""
		Insert value at root of tree
		"""
		self.root = self.put(self.root, value)

	def put(self, N, value):
		"""
		Insert value under given node.
		- Recursive implementation.

		best O(log(n))
		worst O(n)
		"""
		if N is None:
			N = Node(value)
		else:
			if N.value >= value:
				N.left = self.put(N.left, value)
			else:
				N.right = self.put(N.right, value)

		return N

	def delete(self, N, value):
		"""
		Delete value from tree
		"""
		if N is None: return None
		
		if N.value > value:
			N.left = self.delete(N.left, value)
		elif N.value < value:
			N.right = self.delete(N.right, value)
		else:
			if N.left is None:
				return N.right
			elif N.right is None:
				return N.left
			else:
				replace = self.min(N.right)
				N.data = replace.data
				N.right = self.delete(N.right, replace.data)
		return N

	def min(self, N):
		"""
		Find min node in the right subtree
		"""
		if N.left is None:
			return N
		else: 
			return self.min(N.left)

	def min_nonrecursive(self, N):
		while N.left is not None:
			N = N.left
		return N


	def dft_inorder(self, N):
		if N is not None:
			self.dft_inorder(N.left)
			print(N.value, end=" ")
			self.dft_inorder(N.right)

	def dft_preorder(self, N):
		if N is not None:
			print(N.value, end=" ")
			self.dft_preorder(N.left)
			self.dft_preorder(N.right)

	def dft_postorder(self, N):
		if N is not None:
			self.dft_postorder(N.left)
			self.dft_postorder(N.right)
			print(N.value, end=" ")

if __name__ == '__main__':
	BST = BinarySearchTree()
	BST.insert(4)
	BST.insert(9)
	BST.insert(1)
	BST.insert(2)
	BST.insert(5)
	BST.insert(7)
	BST.insert(8)

	print("In Order:")
	BST.dft_inorder(BST.root)
	print("\nPre Order:")
	BST.dft_preorder(BST.root)
	print("\nPost Order:")
	BST.dft_postorder(BST.root)
	print()

	BST.root = BST.delete(BST.root, 1)
	print("\n----- DELETE 1 -----")
	print("In Order:")
	BST.dft_inorder(BST.root)
	print("\nPre Order:")
	BST.dft_preorder(BST.root)
	print("\nPost Order:")
	BST.dft_postorder(BST.root)
	print()
