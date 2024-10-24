#!/usr/bin/env python3

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
 
    # node_set = set() 
    node_table = []

    current = head
    while current:
        # current.display()
        # if current in node_set:
        if current in node_table:
            print("Cycle detected!\nCurrently at:")
            current.display()
            return 1
        else: 
            # node_set.add(current)
            node_table.append(current)
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


# Function to format the output in milliseconds
def convert_to_ms(output):
    result_lines = []
    result_lines.append("\nTiming results:\n")
    result_lines.append(output.splitlines()[0])
    result_lines.append("\t Following times in msec.")
    for line in output.splitlines()[1:]:
        # Identify lines with timing data (lines with "tottime" and "cumtime" columns)
        #if line.strip() and line[0].isdigit():
        if line.strip() and line.strip()[0].isdigit():
            columns = line.split()  # split the line into columns
            try:
                # Convert seconds to milliseconds (multiply by 1000)
                tottime_ms = float(columns[1]) * 1000
                percall_tottime_ms = float(columns[2]) * 1000
                cumtime_ms = float(columns[3]) * 1000
                percall_cumtime_ms = float(columns[4]) * 1000

                # Format the converted times and rebuild the line
                formatted_line = (
                    f"{columns[0]:>9} {tottime_ms:>8.3f} {percall_tottime_ms:>8.3f} "
                    f"{cumtime_ms:>8.3f} {percall_cumtime_ms:>8.3f} {columns[5]}"
                )
                result_lines.append(formatted_line)
            except ValueError as e:
                # If there's an issue converting values, append the original line
                print(f"Error converting line: {line}")
                print(f"Error details: {e}")
                result_lines.append(line)
        else:
            # Non-data lines, just append as-is
            result_lines.append(line)

    return "\n".join(result_lines)



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
    result1_in_ms = convert_to_ms(result1)
    print(result1_in_ms)
#    print(result1)

    print(f'\n\nProfiling {func2.__name__} :')
    result2 = profile_function(func2, *args, **kwargs)
    result2_in_ms = convert_to_ms(result2)
    print(result2_in_ms)
#    print(result2)


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

