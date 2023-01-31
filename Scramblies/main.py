def scramble(word1, word2):
	return not any([word1.count(letter) < word2.count(letter) for letter in set(word2)])