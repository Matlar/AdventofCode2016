import hashlib

with open("input.txt") as f:
	doorID = f.readline().strip()

def md5(message):
	return hashlib.md5(message.encode("utf-8")).hexdigest()

def solve1(hashed):
	password = ""
	index = 0
	while len(password) < 8:
		toHash = hashed + str(index)
		unhashed = md5(toHash)
		if unhashed[:5] == "00000" :
			password += unhashed[5]
		index += 1
	return password

def solve2(hashed):
	password = {"0": "x", "1": "x", "2": "x", "3" : "x", "4" : "x", "5": "x", "6": "x", "7": 'x'}
	index = 0
	solvedPositions = 0
	while solvedPositions < 8:
		toHash = hashed + str(index)
		unhashed = md5(toHash)
		if unhashed[:5] == "00000" :
			position = unhashed[5]
			if position in password and password[position] == 'x':
				password[position] = unhashed[6]
				solvedPositions += 1
		index += 1
	return "".join([value for (key, value) in sorted([(key, value) for (key, value) in password.items()])])

print(solve1(doorID))
print(solve2(doorID))