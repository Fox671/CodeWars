from time import time

def sum_of_intervals(intervals):
    return len(set([i for interval in intervals for i in range(interval[0], interval[1])]))

start = time()
print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (6, 10)]), 8)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
print(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)
end = time()

print(end - start)