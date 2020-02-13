
def winner(board):
	for i in range(3):
		if board[0][i]==board[1][i] and board[0][i]==board[2][i]:
			if board[0][i]=='X':
				return 100
			elif board[0][i]=='O':
				return -100

		if(baord[i][0]==board[i][1] and board[i][2]==board[i][0]):
			if board[i][0]=='X':
				return 100
			elif board[i][0]=='O':
				return -100

	
	if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
		if board[1][1]=='X':
			return 100
		elif board[1][1]=='O':
			return -100

	if board[2][0]==board[1][1] and board[1][1]==board[0][2]:
		if board[1][1]=='X':
			return 100
		elif board[1][1]=='O':
			return -100

	for i in range(3):
		for j in range(3):
			if board[i][j]=='.':
				return -69

	return 0


def minimax(board,depth,maxi):
	if not winner(board)==-69:
		return winner(board)

	if maxi:
		best=-1000
		for i in range(3):
			for j in range(3):
				if possible(i,j):
					board[i][j]='X'
					score=minimax(board,depth+1,false)
					best=max(best,score)
					board[i][j]='.'
		return best
	else:
		best=1000
		for i in range(3):
			for j in range(3):
				if possible(i,j):
					board[i][j]='O'
					score=minimax(board,depth+1,true)
					best=min(best,score)
					board[i][j]='.'
		return best


def ai_move():
	move=[0,0]
	best=-1000
	for i in range(3):
		for j in range(3):
			if possible(i,j):
				board[i][j]='X'
				score=minimax(board,depth+1,false)
				board[i][j]='.'
				if score>best:
					best=score
					move[0]=i
					move[1]=j

	board[move[0]][move[1]]='X'




				


