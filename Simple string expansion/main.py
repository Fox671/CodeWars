def solve(string):
	new_string = ""
	for index, letter in enumerate(string):
		if string[index].isalpha():
			new_string += '"' + letter + '"'
			if string[index + 1] != ')':
				new_string += '+'
		elif string[index].isdigit():
			new_string += letter + '*'
		else:
			new_string += letter
	return eval(new_string)