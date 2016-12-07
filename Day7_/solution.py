import re

def hasAbba(message):
	print(message)
	for i in range(1, len(message) - 2):
		a = message[i - 1]
		b = message[i]
		c = message[i + 1]
		d = message[i + 2]
		if a == d and b == c and a != b:
			return True
	return False
	

with open("input.txt") as f:
	validIPs = 0
	for line in f.readlines():
		print()
		message = line.strip()
		outside = ""
		inside = ""
		within = False
		insideCorrect = True
		outsideCorrect = False
		for char in message:
			if char == "[":
				if hasAbba(outside):
					outsideCorrect = True
				outside = ""
				within = True
			elif char == "]":
				if hasAbba(inside):
					insideCorrect = False
					break
				inside = ""
				within = False
			elif within:
				inside += char
			elif not within:
				outside += char
		if hasAbba(outside):
			outsideCorrect = True

		if insideCorrect and outsideCorrect:
			validIPs += 1
		print(validIPs)

	print("validIPs", validIPs)