real_input = "L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2"
test_input1 = "R2, L3" # should return path_length 5
test_input2 = "R2, R2, R2" # should return path_length 2
test_input3 = "R5, L5, R5, R3" # should return path_length 12
test_input4 = "R8, R4, R4, R8"
# print(directions)
current_pos = [0, 0]
visited = set(tuple(current_pos))

directs = {0: ["UP", (0, 1)],
		   1: ["RIGHT", (1, 0)],
		   2: ["DOWN", (0, -1)],
		   3: ["LEFT", (-1, 0)]
		  }

global current_dir
current_dir = 0
distance = 0

def switchDir(command):
	global current_dir
	if command == "L":
		current_dir = current_dir - 1
		return directs[(current_dir) % 4][1]
	else: # command == "R"
		current_dir = current_dir + 1
		return directs[(current_dir) % 4][1]

def main(directions):
	directions = directions.split(", ")
	for s in directions:
		print(current_pos)
		direction = s[0]
		step_length = int(s[1:])
		new_move = switchDir(direction)
		for dummy_i in range(step_length):
			current_pos[0] += new_move[0]
			current_pos[1] += new_move[1]
			print("I'm at ", tuple(current_pos))
			if tuple(current_pos) not in visited:
				visited.add(tuple(current_pos))
			else:
				print("DEJA VU", current_pos)
				return

# main(test_input1)
# main(test_input2)
# main(test_input3)
# main(test_input4)
main(real_input)
print(current_pos)
print(visited)
print("Length of path: ", abs(current_pos[0]) + abs(current_pos[1]))
if tuple(current_pos) in visited:
	print("I'm back!")