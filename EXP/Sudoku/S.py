def main():
	# Read in the board, creating lists to hold the values of each index
	board = []
	for _ in range(6):
		line = input().split()
		to_add = []
		for item in line:
			if len(item) == 3:
				a,b = item[0],item[2]

				# Empty spots will be considered as zeroes
				if a == '-': a = '0'
				if b == '-': b = '0'

				to_add.append([int(a),int(b)])
			else:
				if item == '-': item = '0'

				to_add.append([int(item)])
		board.append(to_add)

	# Solve the board using a recursive, backtracking dfs
	dfs(board)
	print_board(board)

def dfs(board):
	for i in range(6):
		for j in range(6):
			for p in range(2):
				# If a position only has 1 value, ignore it on the second iteration
				if len(board[i][j]) == 1 and p == 1: continue

				if board[i][j][p] == 0:
					# Try all numbers until one is accepted
					for n in range(1,10):
						if can_place(n,i,j,p,board):
							board[i][j][p] = n

							if dfs(board):
								# The end was reached, return True all the way up
								return True
							else:
								# Reset this position and keep trying
								board[i][j][p] = 0

					# No numbers worked in this position, return up a level
					return False

	# ALl zeroes filled in, a solution was found
	return True


def can_place(n,y,x,p,board):
	# If this is a 2-value position, ensure the top value is smaller
	if len(board[y][x]) == 2:
		p_comp = (p+1) % 2
		if p_comp < p:
			if board[y][x][p_comp] >= n: return False
		elif p_comp > p:
			if board[y][x][p_comp] != 0 and board[y][x][p_comp] <= n: return False

	# Check down the vertical line
	for i in range(6):
		if i == y: continue
		if n in board[i][x]: return False

	# Check across the horizontal line
	for j in range(6):
		if j == x: continue
		if n in board[y][j]: return False

	# Check in the 3x2 rectangle for this position
	r,c = (y//2)*2, (x//3)*3
	for i in range(2):
		for j in range(3):
			if (r+i,c+j) == (y,x): continue
			if n in board[r+i][c+j]: return False

	# No false conditions were met, so return True
	return True

# Print the board according to the original format
def print_board(board):
	output = []
	for i in range(6):
		line = []
		for j in range(6):
			line.append('/'.join(map(str,board[i][j])))
		output.append(' '.join(line))
	print('\n'.join(output))

main()