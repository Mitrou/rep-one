import random
board = []
for x in range(0,5):
	board.append(["O"] * 5)
def print_board(board):
	for row in board:
		print " ".join(row)
print_board(board)
def random_row(board):
	return random.randint(0,len(board)-1)
def random_col(board):
	return random.randint(0,len(board[0])-1)
ship_row = random_row(board)
ship_col = random_col(board)
guess_row = input("Guess Row:")
guess_col = input("Guess Col:")
print ship_row
print ship_col

if guess_row == ship_row and guess_col == ship_col:
	print "Congratulations! You sank my battleship!"
else:
	if guess_row > 0 and guess_row < 6 and guess_col > 0 and guess_col < 6:
		if board[guess_row][guess_col] != "X":
			board[guess_row - 1][guess_col - 1] = "X"
			print "You missed my battleship!"
		else:
			print "You guessed that one already."
	else:
		print "Oops, that's not even in the ocean."
print_board(board)