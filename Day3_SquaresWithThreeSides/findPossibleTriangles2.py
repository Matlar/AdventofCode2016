file = open("input.txt")
possibleTriangles = 0

def possibleTriangle(a, b, c):
	if a + b > c and a + c > b and b + c > a:
		return 1
	return 0

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
while len(line1) > 0:
	line1 = line1.strip().split()
	line2 = line2.strip().split()
	line3 = line3.strip().split()
	a, b, c, d, e, f, g, h, i = int(line1[0]), int(line2[0]), int(line3[0]), int(line1[1]), int(line2[1]), int(line3[1]), int(line1[2]), int(line2[2]), int(line3[2])
	possibleTriangles += possibleTriangle(a, b, c)
	possibleTriangles += possibleTriangle(d, e, f)
	possibleTriangles += possibleTriangle(g, h, i)
	line1 = file.readline()
	line2 = file.readline()
	line3 = file.readline()

file.close()
print(possibleTriangles)