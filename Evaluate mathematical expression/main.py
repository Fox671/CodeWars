import re
def calc(expression: str):
	for new_expression in re.findall(r"\(.*\)", expression):
		expression = expression.replace(new_expression, str(calc(new_expression[1:-1])))
	for new_expression in re.findall(r"(?!^)\d+\.*\d*\s*[\*/]\s*\d+\.*\d*(?!$)", expression):
		expression = expression.replace(new_expression, str(calc(new_expression)))

	numbers = re.findall(r"(?<=\-)\s*\-\d+\.*\d*|^\-\d+\.*\d*|\d+\.*\d*", expression)
	symbols = re.findall(r"(?<=\d)\s*[\+\-\*/]", expression)

	def _calc(numbers, symbols):
		if len(symbols):
			if symbols[0].replace(" ", "") == "+": return float(numbers[0]) + _calc(numbers[1:], symbols[1:])
			elif symbols[0].replace(" ", "") == "-": return float(numbers[0]) - _calc(numbers[1:], symbols[1:])
			elif symbols[0].replace(" ", "") == "*": return float(numbers[0]) * _calc(numbers[1:], symbols[1:])
			elif symbols[0].replace(" ", "") == "/": return float(numbers[0]) / _calc(numbers[1:], symbols[1:])
		else:
			return float(numbers[0])

	return _calc(numbers, symbols)

print(calc("5+(1/5-1)* -4"))             # should equal 2
print(calc("-4"))             # should equal 2
print(calc('8/16'))              # should equal 0.5
print(calc('3 -(-1)'))           # should equal 4
print(calc('2 + -2'))            # should equal 0
print(calc('2 - -5'))         # should equal 13
print(calc('(((10)))'))          # should equal 10
print(calc('3 * 5'))             # should equal 15
print(calc('-7 * -(6 / 3)'))     # should equal 14


# import regex

# expression = "-1"
# numbers = re.findall(r"(?<=\-)\s*\-\d+|\d+", expression)
# symbols = re.findall(r"\-\s*(?=\d+)", expression)

# print(numbers, symbols)