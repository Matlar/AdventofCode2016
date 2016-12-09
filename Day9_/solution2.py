
with open("input.txt") as f:
	for line in f.readlines():	
		answer = 0	
		message = line.strip()
		messageL = len(message)
		operators = []
		index = 0
		inMarker = False
		marker = ""
		for char in message:
			# print(operators)
			# print(answer)
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
			for operator in operators:
				operator[0] -= 1
		# while index < messageL:
		# 	markStart = message.find("(", index, messageL)
		# 	if markStart < index:
		# 		break
		# 	markEnd = message.find(")", markStart, messageL)
		# 	marker = message[markStart + 1: markEnd]
		# 	markL, markR = marker.split("x")
		# 	index = markEnd + int(markL) + 1
		# answer += message[index:]
		
		# print(instruct)
		print("Answer:", answer)