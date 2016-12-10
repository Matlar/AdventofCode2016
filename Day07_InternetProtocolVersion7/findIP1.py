def hasAbba(message):
	for i in range(0, len(message) - 3):
		a = message[i]
		b = message[i + 1]
		c = message[i + 2]
		d = message[i + 3]
		if a == d and b == c and a != b:
			return True
	return False
	

with open("input.txt") as f:
	validIPs = 0
	for line in f.readlines():
		message = line.strip()
		outside = ""
		inside = ""
		within = False
		validIP = False
		for char in message:
			if char == "[":
				if hasAbba(outside):
					validIP = True
				outside = ""
				within = True
			elif char == "]":
				if hasAbba(inside):
					validIP = False
					break
				inside = ""
				within = False
			elif within:
				inside += char
			elif not within:
				outside += char
		if hasAbba(outside):
			validIP = True
		if validIP:
			validIPs += 1
	print("Valid ip's:", validIPs)