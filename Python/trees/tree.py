import sys
from bst import BinarySearchTree

def main():

	s = input('Enter some values to create a BST! >  ')

	nodelst = s.split()

	tree = BinarySearchTree()

	for e in nodelst:
		tree.insert(int(e))

	print(f'Your BST has {tree.visualize()} nodes.')

	"""
	s = input('Enter one more value to insert! >  ')
	node = s.split()[0]
	tree.insert(node)
	"""

	print("Your BST contains the following nodes, in-order:")
	for node in tree:
		print(node)

	s = input('Enter a value to delete >  ')
	delval = int(s)
	tree.delete(delval)


if __name__ == "__main__":
	main()
