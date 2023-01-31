def row_sum_odd_numbers(n):
	start = sum(range(n)) * 2 + 1
	end = start + (n) * 2
	return sum(range(start, end, 2))