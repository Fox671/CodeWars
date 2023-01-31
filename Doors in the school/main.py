def doors(n):
	result = [False for _ in range(n)]
	for i in range(n):
		for j in range(i, n, i + 1):
			result[j] = not result[j]
	return sum(result)