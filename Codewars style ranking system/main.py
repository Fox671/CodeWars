class User():
	RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

	def __init__(self):
		self.rank = -8
		self.progress = 0
	
	def inc_progress(self, rank):
		if rank in self.RANKS:
			if self.rank != 8:
				if self.RANKS.index(self.rank) == self.RANKS.index(rank) + 1:
					self.progress += 1
				elif self.rank == rank:
					self.progress += 3
				elif self.rank < rank:
					self.progress += abs(self.RANKS.index(self.rank) - self.RANKS.index(rank)) ** 2 * 10

			while self.progress >= 100:
				self.rank = self.RANKS[self.RANKS.index(self.rank) + 1]
				self.progress -= 100

			if self.rank >= 8:
				self.rank, self.progress = 8, 0
		else:
			raise Exception("Invalid rank")