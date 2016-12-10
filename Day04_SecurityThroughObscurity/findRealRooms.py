def findCheckSum(message):
	checkSum = ""

	# Find and sort letters after number of occurrences
	occurrences = {}
	for letter in message:
		if letter != "-":
			if letter in occurrences:
				occurrences[letter] += 1
			else:
				occurrences[letter] = 1
	letterList = sorted([(value, key) for (key, value) in occurrences.items()], reverse=True)

	# Find groups of letters with the same number of occurrences
	letters = []
	temp = []
	for i in range(0, len(letterList)):
		# if last element
		if i == len(letterList) - 1:
			if letterList[i][0] < letterList[i - 1][0]:
				letters.append(temp)
				temp = []
			temp.append(letterList[i][1])
			break
		else:
			temp.append(letterList[i][1])
			if letterList[i][0] > letterList[i + 1][0]:
				letters.append(temp)
				temp = []
	if len(temp) > 0:
		letters.append(temp)

	# Sort letters alphabetically, within their group  
	for equalLetters in letters:
		checkSum += ''.join(sorted(equalLetters))
	return checkSum[:5]

# 97-122, a-z, 26 letters
# ord() unicode -> char, chr() char -> unicode
def decrypt(message):
	decrypted = ""
	message, rotation = message
	for letter in message:
		if letter == "-":
			decrypted += " "
		else:
			decrypted += chr((ord(letter) - 97 + rotation) % 26 + 97)
	return decrypted, rotation

with open("input.txt") as f:
	realRoomSidSum = 0
	realRooms = []
	for line in f.readlines():
		encName, secondPart = line.strip().rsplit("-", 1)
		sid, checkSum = secondPart.strip("]").split("[")
		if checkSum == findCheckSum(encName):
			realRoomSidSum += int(sid)
			realRooms.append((encName, int(sid)))
	print(realRoomSidSum)
	for room in realRooms:
		decryptedMessage, rotation = decrypt(room)
		if "north" in decryptedMessage:
			print(decryptedMessage, rotation)
