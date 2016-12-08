def displayScreen():
	for row in screen:
		print(row)

def fillRect(row, col):
	for r in range(row):
		for c in range(col):
			screen[r][c] = "#"

def rotateRow(row, step):
	newRow = ["." for i in range(WIDTH)]
	for col in range(WIDTH):
		if screen[row][col] == "#":
			newRow[(col + step) % WIDTH] = "#"
	for col in range(WIDTH):
		screen[row][col] = newRow[col]

def rotateCol(col, step):
	newCol = ["." for i in range(HEIGHT)]
	for row in range(HEIGHT):
		if screen[row][col] == "#":
			newCol[(row + step) % HEIGHT] = "#"
	for row in range(HEIGHT):
		screen[row][col] = newCol[row]

def countLitPixels():
	litPixels = 0
	for row in range(HEIGHT):
		for col in range(WIDTH):
			if screen[row][col] == "#":
				litPixels += 1
	return litPixels

with open("input.txt") as f:
	WIDTH = 50
	HEIGHT = 6
	screen = [["." for j in range(WIDTH)] for i in range(HEIGHT)]
	for line in f.readlines():		
		instruct = line.strip().split()
		if instruct[0] == "rect":
			row, col = instruct[1].split("x")
			fillRect(int(col), int(row))
		elif instruct[0] == "rotate":
			steps = int(instruct[4])
			dim = int(instruct[2][2:])
			if instruct[1] == "row":
				rotateRow(dim, steps)
			elif instruct[1] == "column":
				rotateCol(dim, steps)
	displayScreen()
	print("Lit pixels:", countLitPixels())
