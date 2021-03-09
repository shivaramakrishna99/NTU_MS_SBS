def coloring(L, colors, numbers):
	board = []
	higher = numbers.index(max(numbers))
	lower = numbers.index(min(numbers))
	for box in range(L*L):
		if box % 2 == 0:
			board.append(colors[higher])
		else:
			board.append(colors[lower])
	for i in range(len(board)):
		print(board[i], end=' ')
		if i % 5 == 4:
			print()

coloring(5, ['R','B'], [12,13])
		
		
