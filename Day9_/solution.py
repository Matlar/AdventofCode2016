

with open("input.txt") as f:
	answer = ""
	for line in f.readlines():		
		message = line.strip()
		messageL = len(message)
		print(messageL)
		index = 0
		while index < messageL:
			print(index)
			markStart = message.find("(", index, messageL)
			if markStart < index:
				break
			answer += message[index:markStart]
			markEnd = message.find(")", markStart, messageL)
			print(markStart + 1)
			print(markEnd)
			marker = message[markStart + 1: markEnd]
			print(marker)
			markL, markR = marker.split("x")
			answer += message[markEnd + 1: markEnd + 1 + int(markL)] * int(markR)
			index = markEnd + int(markL) + 1
		answer += message[index:]
		
		# print(instruct)
	print("Answer:", len(answer))