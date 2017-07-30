class Stack:
	def __init__(self):
		self.top = 1
		self.s = []

	def push(self, x):
		self.s.append(x)
		return self.s

	def pop(self):
		if not self.s:
			raise("Underflow error")
		else:
			self.top = self.top - 1
			return self.s[self.top + 1]


if __name__ == '__main__':
	stack_sample = Stack()
	print(stack_sample.push(1))
	print(stack_sample.push(2))
	print(stack_sample.pop())