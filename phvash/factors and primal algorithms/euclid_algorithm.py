""""
	Program to Calulate the greatest common divisors of two numbers using
	the euclid algorithm.

	Time Complexity: O(logn)

 """

def greatest_common_divisor(a, b):
	while b is not 0:
		remainder = a % b
		# note: GCD(a, b) = GCD(B, remainder)
		a = b
		b = remainder
	return a

if __name__ == '__main__':
	# print(greatest_common_divisor(78489984, 66235938938))
	print(greatest_common_divisor(100, 50))