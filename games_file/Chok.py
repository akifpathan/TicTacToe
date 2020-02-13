import tkinter as tk
import turtle as tl
import time
import random_ai
import real_ai

#current_player="O"
class Board():
    def __init__(self,current_player,master):
        Board.current_player=current_player
        Board.master=master
    cells=[]
    board=[]
    flag=1
    def newboard(self):
        Board.cells.clear()
        Board.board.clear()
        Board.current_player="O"
        for i in range(3):
            Board.cells.append([])
            Board.board.append([])
        for i in range(3):
            for j in range(3):
                Board.cells[i].append(Box(i,j))
                Board.board[i].append(".")

    
class Box():
    #global current_player
    def __init__(self,mrow,mcolumn):
        
        self.row=mrow
        self.column=mcolumn
        self.value=""
        self.label = tk.LabelFrame(master=Board.master, width=235, height=235,bg="Black")
        self.mark=1
        #grid manager to set label localization
        self.label.grid(row=mrow, column=mcolumn)


        #Create button and set it localization. You can change it font without changing size of button, but if You set too big not whole will be visible
         
        self.cell=tk.Button(master=Board.master,
                       bg="Black",
                       command=self.turn,
                       state="normal",
                        activebackground="Black",
                        relief="ridge"
                       )

        #Use sticky to button took up the whole label area
        self.cell.grid(row=mrow, column=mcolumn, sticky='nesw')
        self.sc=tk.Canvas(master=Board.master,width=230,height=230,bd=0,bg="Black")
        self.nop=tl.TurtleScreen(self.sc)
        
        
    def turn(self):
        
        if Board.flag:
            Board.flag=0
            
            self.make_canvas()
            self.draw(Board.current_player)
            
            self.change_player()
            self.checkwin()
            if Board.current_player=="X":
                real_ai.ai_move()
                #random_ai.computers_move()
                self.change_player()
                self.checkwin()
            Board.flag=1
            
    def make_canvas(self):
        self.mark=0
        self.sc.grid(row=self.row,column=self.column,sticky='nsew')
        self.tt=tl.RawTurtle(self.sc)
        self.tt.speed(0)
        self.nop.bgcolor("Black")
        self.tt.color("White")
        
        self.tt.hideturtle()
        
        self.tt.pensize(20)
        
        
        self.value=Board.current_player
        Board.board[self.row][self.column]=Board.current_player
        
     
    def draw(self,x):
        
        if x=="X":
            self.tt.speed(4)
            self.tt.up()
            self.tt.goto(-80,80)
            self.tt.down()
            self.tt.seth(-45)
            self.tt.goto(80,-80)
            self.tt.up()
            self.tt.goto(80,80)
            self.tt.down()
            self.tt.goto(-80,-80)
            
        elif x=="O":
            self.tt.speed(10)
            self.tt.up()
            self.tt.goto(0,80)
            self.tt.down()
            self.tt.circle(-80)
    
    def change_player(self):
        #global current_player
        if Board.current_player == "O":
            Board.current_player = "X"
        elif Board.current_player == "X":
            Board.current_player = "O"
    

        
    def checkwin(self):
        for i in range(3):
            if Board.cells[0][i].value==Board.cells[1][i].value==Board.cells[2][i].value!="":
                for j in range(3):
                    Board.cells[j][i].tt.color("red")
                Board.cells[0][i].tt.up()
                Board.cells[0][i].tt.speed(10)
                Board.cells[1][i].tt.speed(10)
                Board.cells[2][i].tt.speed(10)
                Board.cells[0][i].tt.goto(0,50)
                Board.cells[0][i].tt.down()
                Board.cells[0][i].tt.goto(0,-115)
                Board.cells[1][i].tt.up()
                Board.cells[1][i].tt.goto(0,115)
                Board.cells[1][i].tt.down()
                Board.cells[1][i].tt.goto(0,-115)
                Board.cells[2][i].tt.up()
                Board.cells[2][i].tt.goto(0,115)
                Board.cells[2][i].tt.down()
                Board.cells[2][i].tt.goto(0,-50)
                
                time.sleep(2)
                
                Board.newboard(self)
        for i in range(3):
            if Board.cells[i][0].value==Board.cells[i][1].value==Board.cells[i][2].value !="":
                for j in range(3):
                    Board.cells[i][j].tt.color("red")
                Board.cells[i][0].tt.up()
                Board.cells[i][0].tt.speed(10)
                Board.cells[i][1].tt.speed(10)
                Board.cells[i][2].tt.speed(10)
                Board.cells[i][0].tt.goto(-50,0)
                Board.cells[i][0].tt.down()
                Board.cells[i][0].tt.goto(115,0)
                Board.cells[i][1].tt.up()
                Board.cells[i][1].tt.goto(-115,0)
                Board.cells[i][1].tt.down()
                Board.cells[i][1].tt.goto(115,0)
                Board.cells[i][2].tt.up()
                Board.cells[i][2].tt.goto(-115,0)
                Board.cells[i][2].tt.down()
                Board.cells[i][2].tt.goto(50,0)
                
                time.sleep(2)
                
                Board.newboard(self)
        if Board.cells[0][0].value==Board.cells[1][1].value==Board.cells[2][2].value !="":
            for i in range(3):
                Board.cells[i][i].tt.color("red")
            Board.cells[0][0].tt.speed(10)
            Board.cells[1][1].tt.speed(10)
            Board.cells[2][2].tt.speed(10)
            Board.cells[0][0].tt.up()
            Board.cells[0][0].tt.goto(-50,50)
            Board.cells[0][0].tt.down()
            Board.cells[0][0].tt.goto(115,-115)
            Board.cells[1][1].tt.up()
            Board.cells[1][1].tt.goto(-115,115)
            Board.cells[1][1].tt.down()
            Board.cells[1][1].tt.goto(115,-115)
            Board.cells[2][2].tt.up()
            Board.cells[2][2].tt.goto(-115,115)
            Board.cells[2][2].tt.down()
            Board.cells[2][2].tt.goto(50,-50)
            
            time.sleep(2)
            Board.newboard(self)
        if Board.cells[0][2].value==Board.cells[1][1].value==Board.cells[2][0].value !="":
            
            Board.cells[0][2].tt.speed(10)
            Board.cells[0][2].tt.color("red")
            Board.cells[1][1].tt.speed(10)
            Board.cells[1][1].tt.color("red")
            Board.cells[2][0].tt.speed(10)
            Board.cells[2][0].tt.color("red")
            Board.cells[0][2].tt.up()
            Board.cells[0][2].tt.goto(50,50)
            Board.cells[0][2].tt.down()
            Board.cells[0][2].tt.goto(-115,-115)
            Board.cells[1][1].tt.up()
            Board.cells[1][1].tt.goto(115,115)
            Board.cells[1][1].tt.down()
            Board.cells[1][1].tt.goto(-115,-115)
            Board.cells[2][0].tt.up()
            Board.cells[2][0].tt.goto(115,115)
            Board.cells[2][0].tt.down()
            Board.cells[2][0].tt.goto(-50,-50)
            
            time.sleep(2)
            Board.newboard(self)
                    
        for i in range(3):
            if Board.cells[i][0].value =="" or Board.cells[i][1].value =="" or Board.cells[i][2].value =="":
                break
        else:
            time.sleep(2)
            Board.newboard(self)


 
