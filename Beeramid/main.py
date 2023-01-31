def beeramid(bonus, price):
	result = []
	i = 0
	while sum(result) + (i + 1)**2 <= bonus // price:
		i += 1
		result.append(i**2)
	return i