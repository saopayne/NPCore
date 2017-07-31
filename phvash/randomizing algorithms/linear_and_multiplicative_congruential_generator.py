class Generator:
	def __init__(self, **kwargs):
		self.previous_item = kwargs.get('seed', 0)
		self.constant_one = 3
		self.constant_two = 2
		self.constant_three = 93

	def next_item_linear(self):
		"""  linear congruential generator"""
		random_number = (self.previous_item * self.constant_one + 
							self.constant_two)%(self.constant_three)
		self.previous_item = random_number
		return random_number

	def next_item_mux(self):
		""" multiplication congruential generator """
		random_number = (self.previous_item * self.constant_one + 
							self.constant_two)%(self.constant_three)
		self.previous_item = random_number
		return random_number

if __name__ == '__main__':
	test = Generator(seed=21)
	for i in range(200):
		print(test.next_item_linear())

	print("="*50)

	for i in range(200):
		print(test.next_item_mux())