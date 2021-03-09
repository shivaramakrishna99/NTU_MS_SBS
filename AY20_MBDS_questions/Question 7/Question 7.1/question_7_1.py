def coord_2_ind(coord, dim): #Coordinates to Index
	index = coord[0]
	for x in range(len(coord)-1,0,-1):
		for L in range(x):
			coord[x] = coord[x]*dim[L]
		index = index + coord[x]
	return index


def ind_2_coord(index, dim):  #Index to Coordinates
	divisor = 1
	for L in reversed(range(len(dim))):
		divisor = divisor * dim[L]
	coord = []
	for L in reversed(range(len(dim))):
		divisor = divisor // dim[L]
		axis_coordinate = index // divisor
		index = index - (axis_coordinate * divisor)
		coord.insert(0, axis_coordinate)
	return coord

dim = [50,57]  #Set given dimensions

print('index')  #START - Comment from here to run Index to Coordinates function
f = open("input_coordinates_7_1.txt")
next(f)
for line in f.readlines():
	line = line.strip().split("\t")
	coords = [int(i) for i in line] 
	print(coord_2_ind(coords,dim))
	f.close()  #END


coords = [] #START - Comment from here to run Coordinates to Index function
f = open("input_index_7_1.txt")
next(f)
for line in f.readlines():
	index = int(line.strip()) 
	coord = ind_2_coord(index,dim)
	coords.append(coord)
	f.close()

print("x1	x2")
for coord in coords:
	for axis in coord:
		print(axis, end="	")
	print()



