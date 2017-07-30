def max_subarray_sum(array, n):
    ans = float('-inf')
    for start_index in range(n):
        sum = 0
        for subaray_length in range(1, n+1):
            if subaray_length + start_index <= n:
                sum += array[subaray_length - 1]
                if sum > ans:
                    ans = sum
    return ans

# print(max_subarray_sum([2, 3, 4, 5, 7], 5))
print(max_subarray_sum([3, -2, 5, -1], 4))