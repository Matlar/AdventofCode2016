import re

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

with open("example2.txt") as f:
	validIPs = 0
	for line in f.readlines():
		print()
		message = line.strip()
		outside = ""
		inside = ""
		within = False
		abas = []
		babs = []
		for char in message:
			if char == "[":
				abas.append(findABA(outside))
				outside = ""
				within = True
			elif char == "]":
				babs.append(findBAB(inside))
				inside = ""
				within = False
			elif within:
				inside += char
			elif not within:
				outside += char
		print(abas)
		print(babs)
		for l1 in abas:
			for aba in l1:
				print(aba[0])
				print(aba[1])
				if aba[1] + aba[0] + aba[1] in babs:
					validIPs += 1
		print(validIPs)

	print("validIPs", validIPs)