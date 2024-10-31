import sys
from bst import BinarySearchTree

def main():

    s = input('Enter some values to create a BST! >  ')

    nodelst = s.split()

    tree = BinarySearchTree()

    for e in nodelst:
        tree.insert(int(e))

    print("Your BST contains the following values, in-order:")
    for node in tree:
        print(f'{node}', end = ' ')
    print()

    print("A BFS on your BST shows nodes organized in the following levels, according to the values:")
    tree.treeBFS()

    while(1):

        print('Here\'s a visualization of your tree.')
        tree.visualize()

        s = input('Enter a value to delete >  ')
        try:
            delval = int(s)  # Try to convert input to integer
            tree.delete(delval)
        except ValueError:  # If conversion fails, exit the loop
            print("Exiting.")
            break




if __name__ == "__main__":
    main()
