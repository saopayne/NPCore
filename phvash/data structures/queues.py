class Node:
	def __init__(self, data=None):
		self.next = None
		self.data = data

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_next_node(self, node):
		self.next = node

	def get_next_node(self):
		return self.next

class Queue:
	"""
		Queue implementation using linked list 
		Policy: FIFO
	"""
	def __init__(self):
		# eliminates the need to iterate through the list to get the queue size
		self.length = 0
		self.head = None

	def insert(self, item):
		new_node = Node(item)
		if not self.head:
			# if list is empty, he new nodes takes the first spot
			self.head = new_node
		else:
			# find the last node in the list
			current_node = self.head
			while current_node:
				if not current_node.get_next_node():
					current_node.set_next_node(new_node)
					break
				current_node = current_node.get_next_node()
		self.length += 1

	def remove(self):
		first_node = self.head
		self.head = first_node.get_next_node()
		self.length -= 1
		return first_node.get_data()

class ImprovedQueue:
	"""
		Performs all operations in constant time
		Policy: FIFO
	"""

	def __init__(self):
		self.length = 0
		self.head = None
		self.last_node = None

	def insert(self, item):
		new_node = Node(item)
		if self.length == 0:
			self.head = self.last_node = new_node
		else:
			# update last node
			self.last_node.set_next_node(new_node)
			self.last_node = new_node
		self.length += 1

	def remove(self):
		first_node = self.head
		if self.length == 1:
			self.last_node = None
		self.head = first_node.get_next_node()
		self.length -= 1
		return first_node.get_data()