ERROR = -1
SUCCESS = 0

class simpleFifoQueue:

	def __init__(self, capacity=None):

		self.queue = []
		self.capacity = capacity
		self.head = self.tail = 0


	def simpleEnqueue(self, data):

		if self.capacity is not None:
			if self.capacity == self.tail :
				print("Queue is full.")
				return ERROR
				
		self.queue.append(data)
		self.tail += 1

		print(f"{data} appended to queue.")
		return SUCCESS


	def simpleDequeue(self):

		if self.head == self.tail :
			print("Queue is empty.")
			return None

		deqVal = self.queue.pop(0)
		self.head += 1

		print(f"{deqVal} removed from queue.")
		return deqVal


	def simpleQueueDisplay(self): 

		if self.head == self.tail :
			print("Queue is empty.")

		else:
			for item in self.queue :
				print(item, " <--", end="")
		
			print(f"\nTotal elements: {len(self.queue)}")


	def simpleQueuePeek(self):

		if self.head == self.tail :
			print("Queue is empty.")

		else:
			print(f"Peeking at element at head: {self.queue[0]}")
			return self.queue[0]
			
