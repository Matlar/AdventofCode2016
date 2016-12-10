with open("input.txt") as f:
	lineNr = [{}, {}, {}, {}, {}, {}, {}, {}]
	for line in f.readlines():
		line = line.strip()
		for i in range(8):
			if line[i] in lineNr[i].keys():
				lineNr[i][line[i]] += 1
			else:
				lineNr[i][line[i]] = 1
	mostCommon = ""
	leastCommon = ""
	for letter in lineNr:
		letterFreq = sorted([(value, key) for (key, value) in letter.items()])
		mostCommon += letterFreq[0][1]
		leastCommon += letterFreq[-1][1]
	print("Password according to most common letter", mostCommon)
	print("Password according to least common letter", leastCommon)