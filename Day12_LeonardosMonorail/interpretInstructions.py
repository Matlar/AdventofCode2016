import time

def read(key, dct):
	if key in dct:
		return dct[key]
	else:
		return int(key)

t1 = time.time()
with open("input.txt") as f:
	variables = {"a": 0, "b": 0, "c": 0, "d": 0}
	# Uncomment for part 2
	# variables["c"] = 1
	istrcts = [line.strip().split() for line in f.readlines()]
	istrctL = len(istrcts)
	index = 0
	while index < istrctL:
		istrct = istrcts[index]
		if len(istrct) == 2:
			operation, variable = istrct
			if operation == "inc":
				variables[variable] += 1
			else: # operation == "dec"
				variables[variable] -= 1
		else: # len(istrct) == 3
			operation, arg1, arg2 = istrct
			if operation == "cpy":
				variables[arg2] = read(arg1, variables)
			else: # operation == "jnz"
				arg1 = read(arg1, variables)
				arg2 = read(arg2, variables)
				if arg1 != 0:
					index += arg2 - 1
		index += 1
	print("a contains:", variables["a"])
	print(time.time() - t1)
