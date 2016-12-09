import time
with open("input.txt") as f:
	for line in f.readlines():	
		answer = 0	
		message = line.strip()
		operators = []
		inMarker = False
		marker = ""
		t1  = time.time()
		for char in message:
			if char == "(":
				inMarker = True
			elif char == ")":
				inMarker = False
				markL, markR = marker.split("x")
				operators.append([int(markL) + 1, int(markR)])
				marker = ""
			elif inMarker:
				marker += char
			else:
				dLength = 1
				for operator in operators:
					if operator[0] > 0:
						dLength *= operator[1]
				answer += dLength
			newOperators = []
			for operator in operators:
				operator[0] -= 1
				if operator[0] > 0:
					newOperators.append(operator)
			operators = newOperators
		print("Answer:", answer)
		print(time.time() - t1)