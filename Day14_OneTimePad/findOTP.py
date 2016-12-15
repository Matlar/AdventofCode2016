import hashlib, time
t1 = time.time()

salt = "ngcjuoqr"

def md5(message, key_stretching):
	h = hashlib.md5(message.encode("utf-8")).hexdigest()
	if key_stretching:
		for dummy_i in range(2016):
			h = hashlib.md5(h.encode("utf-8")).hexdigest()
	return h

def findKeys(salt):
	triplets = {}
	keys = []
	index = 0
	stop_index = -1

	while True:
		if stop_index == index:
			return keys
		# Change key_stretching to True for part 2
		key_stretching = True
		hex_hash = md5(salt + str(index), key_stretching)

		fives = []
		triple = ""
		multiple = " "
		found_triple = False
		for char in hex_hash:
			if char == multiple[0]:
				multiple += char
				if len(multiple) == 3 and not found_triple:
					triple = multiple
					found_triple = True
				elif len(multiple) == 5:
					fives.append(multiple)
			else:
				multiple = char

		for penta in fives:
			for key in list(triplets.keys()):
				if penta[0:3] == triplets[key][2]:
					keys.append((triplets[key][0], key))
					triplets.pop(key)
					if len(keys) == 64:
						stop_index = index + 1000

		for key in list(triplets.keys()):
			if triplets[key][1] == index:
				triplets.pop(key)

		if found_triple:
			triplets[hex_hash] = (index, index + 1000, triple)

		index += 1
	return keys

found_keys = sorted(findKeys(salt))
print("Found keys:", found_keys)
print("\nNumber of keys:", len(found_keys))
print("64th key(index, key):", found_keys[63])
print(time.time() - t1)