import time
with open("input.txt") as f:
	# Bot 0 to 209, 210 bots in total
	# Output 0 to 20. 21 in total
	t1  = time.time()
	bots = [[] for i in range(231)] #210 originally
	instructs = [{"lTo": None, "hTo": None} for i in range(210)]
	instructionStack = []
	for line in f.readlines():
		answer = ""
		instruction = line.strip().split()
		instructType = instruction[0]
		if instructType == "bot":
			bot = int(instruction[1])
			lTo = int(instruction[6])
			hTo = int(instruction[-1])
			lType = instruction[5]
			hType = instruction[-2]
			if lType == "bot":
				instructs[bot]["lTo"] = lTo
			else: #lType == "output"
				instructs[bot]["lTo"] = lTo + 210
			if hType == "bot":
				instructs[bot]["hTo"] = hTo
			else: #hType == "output"
				instructs[bot]["hTo"] = hTo + 210
		else: # instructType == "value"
			value = int(instruction[1])
			bot = int(instruction[-1])
			bots[bot].append(value)
			if len(bots[bot]) == 2:
				instructionStack.append(bot)
	keyBot = -1
	print(bots)
	print(instructs)
	print(instructionStack)
	while len(instructionStack) > 0:
		# print(len(instructionStack))
		# print(bots)
		# Move around values until 
		# you find value 61 and value 17 in the same bot
		currentBot = instructionStack.pop()
		high = max(bots[currentBot])
		low = min(bots[currentBot])
		bots[currentBot] = []
		if high == 61 and low == 17:
			keyBot = currentBot
			# break			
		lTo = instructs[currentBot]["lTo"]
		hTo =  instructs[currentBot]["hTo"]
		print(lTo, hTo)
		bots[lTo].append(low)
		bots[hTo].append(high)
		if len(bots[lTo]) == 2 and lTo < 210:
			instructionStack.append(lTo)
		if len(bots[hTo]) == 2 and hTo < 210:
			instructionStack.append(hTo)
	print(bots)
	print(instructionStack)
	print("Keybot:", keyBot)
	print("Product of output 1, 2 & 3:", bots[210][0]*bots[211][0]*bots[212][0])
	print(time.time() - t1)

