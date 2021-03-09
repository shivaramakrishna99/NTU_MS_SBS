from itertools import permutations

def operation_sum(path):
	op_sum = 1
	row = 1
	for char in path:
		if char == 'R':
			row_value = row
			op_sum += row_value
		elif char == 'D':
			row += 1
			row_value = row
			op_sum += row_value
	return op_sum
	
def possible_paths(m,n,sval):
	init_path = 'R'*(m-1) + 'D'*(n-1) 
	all_paths = [''.join(char) for char in set(permutations(init_path))]
	for path in all_paths:
		operation_sum(path)
		if (operation_sum(path) == sval):
			print(sval, " ", path)

possible_paths(7,7,50)
#possible_paths(9,9,90)
#possible_paths(9,9,110)

		
