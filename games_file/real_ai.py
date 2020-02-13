import Chok


def possible(i,j):
	return Chok.Board.board[i][j]=="."

def winner():
	for i in range(3):
		if Chok.Board.board[0][i]==Chok.Board.board[1][i] and Chok.Board.board[0][i]==Chok.Board.board[2][i]:
			if Chok.Board.board[0][i]=="X":
				return 100
			elif Chok.Board.board[0][i]=="O":
				return -100

		if(Chok.Board.board[i][0]==Chok.Board.board[i][1] and Chok.Board.board[i][2]==Chok.Board.board[i][0]):
			if Chok.Board.board[i][0]=="X":
				return 100
			elif Chok.Board.board[i][0]=="O":
				return -100

	
	if Chok.Board.board[0][0]==Chok.Board.board[1][1] and Chok.Board.board[1][1]==Chok.Board.board[2][2]:
		if Chok.Board.board[1][1]=="X":
			return 100
		elif Chok.Board.board[1][1]=="O":
			return -100

	if Chok.Board.board[2][0]==Chok.Board.board[1][1] and Chok.Board.board[1][1]==Chok.Board.board[0][2]:
		if Chok.Board.board[1][1]=="X":
			return 100
		elif Chok.Board.board[1][1]=="O":
			return -100

	for i in range(3):
		for j in range(3):
			if Chok.Board.board[i][j]==".":
				return -69

	return 0


def minimax(depth,maxi):
	if not winner()==-69:
		return winner()

	if maxi:
		best=-1000
		for i in range(3):
			for j in range(3):
				if possible(i,j):
					Chok.Board.board[i][j]="X"
					score=minimax(depth+1,False)
					best=max(best,score)
					Chok.Board.board[i][j]="."
		return best
	else:
		best=1000
		for i in range(3):
			for j in range(3):
				if possible(i,j):
					Chok.Board.board[i][j]="O"
					score=minimax(depth+1,True)
					best=min(best,score)
					Chok.Board.board[i][j]="."
		return best


def ai_move():
	move=[0,0]
	best=-1000
	for i in range(3):
		for j in range(3):
			if possible(i,j):
				Chok.Board.board[i][j]="X"
				score=minimax(0,False)
				Chok.Board.board[i][j]="."
				if score>best:
					best=score
					move[0]=i
					move[1]=j

	x=move[0]
	y=move[1]
	Chok.Board.board[x][y]="X"
	Chok.Board.cells[x][y].make_canvas()
	Chok.Board.cells[x][y].draw(Chok.Board.current_player)



				


