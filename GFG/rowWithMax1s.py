def rowWithMax1s(self,arr, n, m):
	# code here
	max_sum = 0
	j = 0
	for i in range(n):
	    if max_sum < sum(arr[i]):
	        max_sum = sum(arr[i])
	        j = i
	if max_sum == 0:
	    j = -1
	return j