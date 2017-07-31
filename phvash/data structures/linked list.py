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


class LinkedList:
	def __init__(self):
		self.head = Node()

	def insert(self, data):
		""" 
			inserts a new element at the root of the list
			i.e the new element becomes the first element in the list

		 """
		temp = Node(data)
		temp.set_next_node(self.head)
		self.head = temp

	def alternative_insert(self, data):
		""" 
			Inserts the new item at the tip of the list
			i.e the new element becomes the last item in the list

		"""

		current_node = self.head

		while current_node.get_next_node():
			current_node = current_node.get_next_node()
		
		current_node.set_data(data)
		current_node.set_next_node(Node())
		print("current_node.get_data(): ", current_node.get_data())
		print("nxt data: ", current_node.get_next_node().get_data())

	def remove(self, data):
		""" Removes the first occurence of an item in the list"""

		current_node = self.head
		previous_node = None

		# using .get_next_node as check in the while loop prevents 
		# the need for a try block since for the last node, 
		# get_next_node will return None,
		# therefore, last_node.get_data never gets called
		# note: last_node.get_data will raise AttributeError since
		# 		since the node is set to None
		
		while current_node.get_next_node():
			if current_node.get_data() is not data:
				previous_node = current_node
				current_node = current_node.get_next_node()
			else:
				previous_node.set_next_node(current_node.get_next_node())
				break # this prevents the removal of all occurences of data in the list

	def size(self):
		count = 0
		current_node = self.head
		while current_node.get_next_node():
			current_node = current_node.get_next_node()
			count += 1
		return count

	def search(self, item):
		current_node = self.head
		while current_node.get_next_node():
			if current_node.get_data() is item:
				return True
			current_node = current_node.get_next_node()
		return False

	def update(self, old_item, new_item):
		""" Updates the first occurences of old_item in the list with new_item """
		current_node = self.head

		while current_node.get_next_node():
			if current_node.get_data() is old_item:
				current_node.set_data(new_item)
				break
			current_node = current_node.get_next_node()

if __name__ == '__main__':
	# test node
	test_node = Node('content one')
	print(test_node.get_data())
	test_node.set_data('new content one')
	print(test_node.get_data())

	test_list = LinkedList()
	test_list.insert('Hello') # insert first item
	test_list.insert('World') # insert second item

	first_item = test_list.head
	print(first_item.get_data())
	second_item = first_item.get_next_node()
	print(second_item.get_data())
	third_item = second_item.get_next_node()
	print(third_item.get_data())
	print("size", test_list.size())
	

	test_list.remove("Hello")
	print("new size", test_list.size())
	first_item = test_list.head
	print(first_item.get_data())
	second_item = first_item.get_next_node()
	print(second_item.get_data())

	print(test_list.search("apple"))
	print(test_list.search("World"))


	test_list.remove("sajhasj")
	test_list.update("World", "Bye")
	first_item = test_list.head
	print(first_item.get_data())

	test_list.alternative_insert("See Ya")
	print("new size", test_list.size())
	first_item = test_list.head
	print(first_item.get_data())
	second_item = first_item.get_next_node()
	print(second_item.get_data())


