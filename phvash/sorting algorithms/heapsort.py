"""
Max-Heapify (A, i):
    left ← 2*i // ← means "assignment"
    right ← 2*i + 1
    largest ← i
    
    if left ≤ heap_length[A] and A[left] > A[largest] then:
        largest ← left
    if right ≤ heap_length[A] and A[right] > A[largest] then:
        largest ← right
    
    if largest ≠ i then:
        swap A[i] and A[largest]
        Max-Heapify(A, largest)

"""

def max_heapify(A, i):
	# left_child_index = 2 * i
	# right_child_index = (2 * i) +1
	# left_child = A[left_child_index]
	# right_child = A[right_child_index]
	# parent = A[i]
	# largest = parent

	# if left_child_index <= len(A) and left_child > parent:
	# 	largest = left_child
	# if right_child_index <= len(A) and right_child > largest:
	# 	largest = right_child

	# if parent != largest:
	# 	A[i] = largest
	# 	max_heapify(A, )

	left = 2 * i
	right = (2 * i) + 1
	largest = i

	if left <= len(A) and A[left] > A[largest]:
		largest = left
	if right <= len(A) and A[right] > A[largest]:
		largest = right

	if largest != i:
		A[i] = A[largest]
		max_heapify(A, largest)


def build_max_heap(a):
	heap_size = len(a)
	for i in range(len(a)//2, 0, -1):
		max_heapify(a, i)
	print(a)

def heap_sort(a):
	build_max_heap(a)
	for i in (len(a), 1, -1):
		heap_size = heap_size - 1
		max_heapify(a, 1)

if __name__ == '__main__':
	build_max_heap([5,2,1,3,4])