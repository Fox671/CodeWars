from time import time

def elder_age(m, n, l, t):
	m, n = sorted([m, n])

	k = 2
	while k * 2 <= m:
		k *= 2

	return 

start_time = time()
print(elder_age(8, 5, 1, 100), 5)
print(elder_age(8, 8, 0, 100007), 224)
print(elder_age(25,31,0,100007), 11925)
print(elder_age(5,45,3,1000007), 4323)
print(elder_age(31, 39, 7, 2345), 1586)
print(elder_age(545,435,342,1000007), 808451)
print(elder_age(28827050410, 35165045587, 7109602, 13719506), 5456283)
end_time = time()

print(end_time - start_time)