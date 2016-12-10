def findABA(message):
	abas = []
	for i in range(len(message) - 2):
		a = message[i]
		b = message[i + 1]
		c = message[i + 2]
		if a == c and a != b:
			abas.append(a+b+c)
	return abas

def findBAB(message):
	return findABA(message)

with open("input.txt") as f:
	validIPs = 0
	for line in f.readlines():
		message = line.strip()
		outside = ""
		inside = ""
		within = False
		abas = []
		babs = []
		for char in message:
			if char == "[":
				outsideABAS = findABA(outside)
				for foundABA in outsideABAS:
					abas.append(foundABA)
				outside = ""
				within = True
			elif char == "]":
				insideABAS = findBAB(inside)
				for foundBAB in insideABAS:
					babs.append(foundBAB)
				inside = ""
				within = False
			elif within:
				inside += char
			elif not within:
				outside += char
		outsideABAS = findABA(outside)
		for foundABA in outsideABAS:
			abas.append(foundABA)
		for aba in abas:
			if aba[1] + aba[0] + aba[1] in babs:
				validIPs += 1
				break
	print("Valid ip's:", validIPs)