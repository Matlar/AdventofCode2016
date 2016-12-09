import time
with open("input.txt") as f:
	answer = ""
	for line in f.readlines():		
		message = line.strip()
		messageL = len(message)
		index = 0
		t1 = time.time()
		while index < messageL:
			markStart = message.find("(", index, messageL)
			if markStart < index:
				break
			answer += message[index:markStart]
			markEnd = message.find(")", markStart, messageL)
			marker = message[markStart + 1: markEnd]
			markL, markR = marker.split("x")
			answer += message[markEnd + 1: markEnd + 1 + int(markL)] * int(markR)
			index = markEnd + int(markL) + 1
		answer += message[index:]
	print("Answer:", len(answer))
	print(time.time() - t1)