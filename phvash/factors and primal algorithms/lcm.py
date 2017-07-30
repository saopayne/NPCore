from euclid_algorithm import greatest_common_divisor

"""
LCM(A, B) = 	A * B
			  ----------
			  GCD(A, B)

"""

def lcm(a, b):
	return (a / greatest_common_divisor(a, b)) * b

if __name__ == '__main__':
	print(lcm(10000, 20000))