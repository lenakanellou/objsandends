import cProfile
import pstats
import io
import sys
import random

class listNode():

	def __init__(self, key, val, nextp=None):
		self.key = key
		self.val = val
		self.nextp = nextp

	def display(self):
		print(f'Node with key {self.key} and value {self.val}.')


def random_list_create(elemnum, cycle=0):
    # Check if num_elements is an integer
    if not isinstance(elemnum, int):
        raise ValueError("num_elements must be an integer.")

    if elemnum <= 0:
        return None
    
    # Generate unique keys
    keys = random.sample(range(1, elemnum + 1), elemnum)  # unique keys
    values = [random.randint(1, 100) for _ in range(elemnum)]  # random values

    if cycle == 1 and elemnum > 2:
        loop_node_num = random.randint(1, elemnum-1)
    else:
        loop_node_num = None

    loop_node = None

    # Create the linked list
    head = listNode(keys[0], values[0])  # Create the head node
    current = head

    for i in range(1, elemnum):
        if i == elemnum-1:
            new_node = listNode(keys[i], values[i], loop_node)
        else:
            new_node = listNode(keys[i], values[i])
            if i == loop_node_num:
                loop_node = new_node
                print(f'Loop node ID is : {i}.\nLoop starts at:')
                loop_node.display()
        current.nextp = new_node  # Connect the current node to the new node
        current = new_node  # Move to the new node

    return head  # Return the head of the linked list


def display_list(head):
	# Check if head is a listNode instance or None
    if not isinstance(head, (listNode, type(None))):
        raise ValueError("head must be a listNode instance or None.")
    
    current = head
    while current:
        current.display()
        current = current.nextp


def cycle_check_brute(head):
    # Check if head is a listNode instance or None
    if not isinstance(head, (listNode, type(None))):
        raise ValueError("head must be a listNode instance or None.")
 
    node_set = set() 

    current = head
    while current:
        # current.display()
        if current in node_set:
            print("Cycle detected!\nCurrently at:")
            current.display()
            return 1
        else: 
            node_set.add(current)
        current = current.nextp
    print("Reached end of list. No cycles.")
    return 0

def cycle_check_floyd(head):
    # Check if head is a listNode instance or None
    if not isinstance(head, (listNode, type(None))):
        raise ValueError("head must be a listNode instance or None.")

    hare = head.nextp.nextp
    tortoise = head.nextp

    prev_hare = prev_tortoise = None

    while hare != tortoise and hare != None:
        prev_hare = hare
        prev_tortoise = tortoise
        hare = hare.nextp.nextp
        tortoise = tortoise.nextp

    if hare != None:
        print("Cycle detected!\nhare and tortoise pointers currently at:")
        hare.display()
        return 1
    print("Reached end of list. No cycles.")
    return 0   


def profile_function(func, *args, **kwargs):
    """
    Profiles the given function and prints the profiling results.
    
    Parameters:
    func: function to be profiled
    *args: arguments for the function
    **kwargs: keyword arguments for the function
    """
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Run the function
    func(*args, **kwargs)
    
    profiler.disable()

    # Capture the profile stats to a stream
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats('cumulative')
    stats.print_stats()

    # Output the profiling results
    return stream.getvalue()


def contrast_functions(func1, func2, *args, **kwargs):
    """
    Profiles and contrasts two functions.
    
    Parameters:
    func1: First function to profile
    func2: Second function to profile
    *args: arguments for both functions
    **kwargs: keyword arguments for both functions
    """
    print(f'\n\nProfiling {func1.__name__} :')
    result1 = profile_function(func1, *args, **kwargs)
    print(result1)
    
    print(f'\n\nProfiling {func2.__name__} :')
    result2 = profile_function(func2, *args, **kwargs)
    print(result2)


def main(elemnum, cycle):

	head = random_list_create(elemnum, cycle)

	# contrast_functions(func1, func2)
	contrast_functions(cycle_check_brute, cycle_check_floyd, head)



if __name__ == "__main__":
    # Check if exactly two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python my_script.py <arg1> <arg2>")
        sys.exit(1)  # Exit with a non-zero status code

    # Retrieve arguments from sys.argv
    elemnum = int(sys.argv[1])
    cycle = int(sys.argv[2])

    # Call the main function with the arguments
    main(elemnum, cycle)
