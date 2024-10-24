import math

class BinarySearchTree:

	# First, a node class is provided, together with essential, 
	# useful methods. This is the class that will be used to 
	# create the tree and is internal to the BinarySearchTree class.

	class bstNode:
		def __init__(self, val, leftp=None, rightp=None):
			self.val = val
			self.leftp = leftp
			self.rightp = rightp

		def getVal(self):
			return self.val

		def setVal(self, newval):
			self.val = newval

		def leftChild(self):
			return self.leftp

		def rightChild(self):
			return self.rightp

		def setLeftChild(self, newleft):
			self.leftp = newleft

		def setRightChild(self, newright):
			self.rightp = newright

		def __iter__(self):
			if self.leftp != None:
				for node in self.leftp:
					yield node

			yield self.val

			if self.rightp != None:
				for node in self.rightp:
					yield node

		def nodeHeight(self):
			if self is None:
				return 0
			else:
				lh = self.leftp.nodeHeight() if self.leftp else 0
				rh 	= self.rightp.nodeHeight() if self.rightp else 0
				return 1 + max(lh, rh)

	# From here on, the methods of the BinarySearchTree class are defined.
	
	def __init__(self, rootnode=None):
		self.root = rootnode
		self.n = 0

	def treeHeight(self):
		return self.root.nodeHeight()

	def visualize(self):
		depth = self.treeHeight()
		width = 2**depth - 1	
		print(f'This is your BST, of height {depth}')

		def __by_level(node, level, pos, treearray):
			if node is None:
				return None

			if level >= len(treearray):
				return None

			if pos < 0 or pos >= len(treearray[level]):
				return None
			
			treearray[level][pos] = str(node.val)
			__by_level(node.leftp, level + 1, pos - 2**(depth - level - 1), treearray)
			__by_level(node.rightp, level + 1, pos + 2**(depth - level - 1), treearray)


		treelevels = [[" " for _ in range(width)] for _ in range(depth)]	
		__by_level(self.root, 0, width // 2, treelevels)

		for level in treelevels:
			print("".join(level))
		
		return self.n


	def insert(self, val):
		
		def __insert(root, val):
			if root == None:
				return BinarySearchTree.bstNode(val)

			if root.getVal() == val:
				return None

			if val < root.getVal():
				root.setLeftChild(__insert(root.leftChild(),val))
			else:
				root.setRightChild(__insert(root.rightChild(),val))
			return root

		inserted = __insert(self.root, val)

		if inserted:
			self.root = inserted
			self.n = self.n + 1
		else:
			print(f'{__name__}: value already in tree!')


	def search(self, val):

		def __bstsearch(root, val):
			if root == None:
				return None
			if root.getVal() == val:
				return root

			if val < root.getVal() :
				root = __bstsearch(root.leftp, val)
			else:
				root = __bstsearch(root.rightp, val)
			return root

	def delete(self, val):
		delnode = self.search(val)
		if delnode == None:
			print('Node not found')
		else:
			print(delnode.getVal())

	def __iter__(self):
		if self.root != None:
			return self.root.__iter__()

		else:
			return [].__iter__()
