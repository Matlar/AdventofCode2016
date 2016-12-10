file = open("input.txt")
possibleTriangles = 0

line = file.readline()
while len(line) > 0:
	triangle = line.strip().split()
	a, b, c = int(triangle[0]), int(triangle[1]), int(triangle[2])
	if a + b > c and a + c > b and b + c > a:
		possibleTriangles += 1
	line = file.readline()

file.close()
print(possibleTriangles)