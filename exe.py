from tkinter  import *
import random
import time
class chess:
    pass
Gsteps=[[]]
Gselect=[[]]
square=[[],[],[],[],[],[],[],[]]
Player=[2]
Extra_turn=[0,(0,0)]
Eat=[0]
anime=[0]
save_and_load_board=[2,[]]
class checkers:
    def __init__(self,color):
        self.color=color
        self.king=False
    def gking(self):
        self.king=True
def copyofcheckers(obj,board):
    if obj!=None:
        s=checkers(obj.color)
        if obj.king==True:
            s.gking()
        return s
    else:
        return obj
def copyofboard(board):
    board2=[]
    for i in range(len(board)):
        board2+=[[]]
        for j in range(len(board[i])):
            board2[i]+=[copyofcheckers(board[i][j],board)]
    return board2
def change_square(board):
    for i in range(len(square)):
        square[i]=board[i]
def find_all_available_moves(color,board):
    steps=find_all_steps(color,board)
    esteps=[i for i in steps if i[4]==True]
    if len(esteps)>0:
        return esteps
    return steps
def enemy(color):
    if color=="black":
        return "white"
    else:
        return "black"
def calculate_Best_Move_SAI3(color,board,moves):
    bestMoves = []
    bestCount = float("-inf")
    for i in moves:
        b2=copyofboard(board)
        move_on_board(i[0],i[1],i[2],i[3],i[4],b2)
        if i[4]==False:
            enemymove=calculate_Best_Move_for_one(enemy(color),b2,find_all_available_moves(enemy(color),b2))
            if enemymove!=None:
                move_on_board(enemymove[0],enemymove[1],enemymove[2],enemymove[3],enemymove[4],b2)
                if enemymove[4]==True:
                    esteps=find_select_step_in_steps(enemymove[2],enemymove[3],find_all_steps(enemy(color),b2),True)
                    while(len(esteps)>0):
                        j=calculate_Best_Move_for_one(enemy(color),b2,esteps)
                        move_on_board(j[0],j[1],j[2],j[3],j[4],b2)
                        esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(enemy(color),b2),True)
            c=calculateBoard(b2,color)
        else:
            esteps=find_select_step_in_steps(i[2],i[3],find_all_steps(color,b2),True)
            while(len(esteps)>0):
                j=calculate_Best_Move_for_one(color,b2,esteps)
                move_on_board(j[0],j[1],j[2],j[3],j[4],b2)
                esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(color,b2),True)
            enemymove=calculate_Best_Move_for_one(enemy(color),b2,find_all_available_moves(enemy(color),b2))
            if enemymove!=None:
                move_on_board(enemymove[0],enemymove[1],enemymove[2],enemymove[3],enemymove[4],b2)
                if enemymove[4]==True:
                    esteps=find_select_step_in_steps(enemymove[2],enemymove[3],find_all_steps(enemy(color),b2),True)
                    while(len(esteps)>0):
                        j=calculate_Best_Move_for_one(enemy(color),b2,esteps)
                        move_on_board(j[0],j[1],j[2],j[3],j[4],b2)
                        esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(enemy(color),b2),True)
            c=calculateBoard(b2,color)
        if c>bestCount:
            bestCount=c
            bestMoves=[i]
        elif c==bestCount:
            bestMoves+=[i]
    return random.choice(bestMoves)
def calculate_Best_Move_for_one(color,board,moves):
    bestMoves = []
    bestCount = float("-inf")
    for i in moves:
        b2=copyofboard(board)
        move_on_board(i[0],i[1],i[2],i[3],i[4],b2)
        if i[4]==False:
            c=calculateBoard(b2,color)
        else:
            esteps=find_select_step_in_steps(i[2],i[3],find_all_steps(color,b2),True)
            while(len(esteps)>0):
                j=calculate_Best_Move_for_one(color,b2,esteps)
                move_on_board(j[0],j[1],j[2],j[3],j[4],b2)
                esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(color,b2),True)
            c=calculateBoard(b2,color)
        if c>bestCount:
            bestCount=c
            bestMoves=[i]
        elif c==bestCount:
            bestMoves+=[i]
    if len(bestMoves)>0:
        return random.choice(bestMoves)
    else:
        return None
def calculate_Best_Move(color,board,moves):
    bestMoves = []
    bestCount = float("-inf")
    for i in moves:
        b2=copyofboard(board)
        move_on_board(i[0],i[1],i[2],i[3],i[4],b2)
        if i[4]==False:
            min_move_count=float("inf")
            for enemymove in find_all_available_moves(enemy(color),b2):
                b3=copyofboard(b2)
                if enemymove!=None:
                    move_on_board(enemymove[0],enemymove[1],enemymove[2],enemymove[3],enemymove[4],b3)
                    if enemymove[4]==True:
                        esteps=find_select_step_in_steps(enemymove[2],enemymove[3],find_all_steps(enemy(color),b3),True)
                        while(len(esteps)>0):
                            j=calculate_Best_Move_for_one(enemy(color),b3,esteps)
                            move_on_board(j[0],j[1],j[2],j[3],j[4],b3)
                            esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(enemy(color),b3),True)
                c2max = float("-inf")
                for my_after_enemy_move in find_all_available_moves(color,b3):
                    b4=copyofboard(b3)
                    if my_after_enemy_move!=None:
                        move_on_board(my_after_enemy_move[0],my_after_enemy_move[1],my_after_enemy_move[2],my_after_enemy_move[3],my_after_enemy_move[4],b4)
                        if my_after_enemy_move[4]==True:
                            esteps=find_select_step_in_steps(i[2],i[3],find_all_steps(color,b4),True)
                            while(len(esteps)>0):
                                j=calculate_Best_Move_for_one(color,b4,esteps)
                                move_on_board(j[0],j[1],j[2],j[3],j[4],b4)
                                esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(color,b4),True)
                    enemy_after_my_move=calculate_Best_Move_for_one(enemy(color),b4,find_all_available_moves(enemy(color),b4))
                    if enemy_after_my_move!=None:
                        move_on_board(enemy_after_my_move[0],enemy_after_my_move[1],enemy_after_my_move[2],enemy_after_my_move[3],enemy_after_my_move[4],b4)
                        if enemy_after_my_move[4]==True:
                            esteps=find_select_step_in_steps(i[2],i[3],find_all_steps(enemy(color),b4),True)
                            while(len(esteps)>0):
                                j=calculate_Best_Move_for_one(enemy(color),b4,esteps)
                                move_on_board(j[0],j[1],j[2],j[3],j[4],b4)
                                esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(enemy(color),b4),True)
                    c2=calculateBoard(b4,color)
                    if c2>c2max:
                        c2max=c2
                if c2max<min_move_count:
                    min_move_count=c2max
            c=min_move_count
        else:
            esteps=find_select_step_in_steps(i[2],i[3],find_all_steps(color,b2),True)
            while(len(esteps)>0):
                j=calculate_Best_Move_for_one(color,b2,esteps)
                move_on_board(j[0],j[1],j[2],j[3],j[4],b2)
                esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(color,b2),True)
            min_move_count=float("inf")
            for enemymove in find_all_available_moves(enemy(color),b2):
                c2max = float("-inf")
                b3=copyofboard(b2)
                if enemymove!=None:
                    move_on_board(enemymove[0],enemymove[1],enemymove[2],enemymove[3],enemymove[4],b3)
                    if enemymove[4]==True:
                        esteps=find_select_step_in_steps(enemymove[2],enemymove[3],find_all_steps(enemy(color),b3),True)
                        while(len(esteps)>0):
                            j=calculate_Best_Move_for_one(enemy(color),b3,esteps)
                            move_on_board(j[0],j[1],j[2],j[3],j[4],b3)
                            esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(enemy(color),b3),True)
                for my_after_enemy_move in find_all_available_moves(color,b3):
                    b4=copyofboard(b3)
                    if my_after_enemy_move!=None:
                        move_on_board(my_after_enemy_move[0],my_after_enemy_move[1],my_after_enemy_move[2],my_after_enemy_move[3],my_after_enemy_move[4],b4)
                        if my_after_enemy_move[4]==True:
                            esteps=find_select_step_in_steps(i[2],i[3],find_all_steps(color,b4),True)
                            while(len(esteps)>0):
                                j=calculate_Best_Move_for_one(color,b4,esteps)
                                move_on_board(j[0],j[1],j[2],j[3],j[4],b4)
                                esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(color,b4),True)
                    enemy_after_my_move=calculate_Best_Move_for_one(enemy(color),b4,find_all_available_moves(enemy(color),b4))
                    if enemy_after_my_move!=None:
                        move_on_board(enemy_after_my_move[0],enemy_after_my_move[1],enemy_after_my_move[2],enemy_after_my_move[3],enemy_after_my_move[4],b4)
                        if enemy_after_my_move[4]==True:
                            esteps=find_select_step_in_steps(i[2],i[3],find_all_steps(enemy(color),b4),True)
                            while(len(esteps)>0):
                                j=calculate_Best_Move_for_one(enemy(color),b4,esteps)
                                move_on_board(j[0],j[1],j[2],j[3],j[4],b4)
                                esteps=find_select_step_in_steps(j[2],j[3],find_all_steps(enemy(color),b4),True)
                    c2=calculateBoard(b4,color)
                    if c2>c2max:
                        c2max=c2
                if c2max<min_move_count:
                    min_move_count=c2max
            c=min_move_count
        if c>bestCount:
            bestCount=c
            bestMoves=[i]
        elif c==bestCount:
            bestMoves+=[i]
    return random.choice(bestMoves)
def SAI3(color):
    e=0
    board=square
    steps=find_all_available_moves(color,board)
    step=calculate_Best_Move_SAI3(color,board,steps)
    board=final_move_on_board(step[0],step[1],step[2],step[3],step[4],board)
    if step[4]==True:
        steps=find_select_step_in_steps(step[2],step[3],find_all_steps(color,board),True)
        if len(steps)>0:
            e=1
            #print(color+" бъет другую шашку и перемещаеться из ("+str(step[0])+";"+str(step[1])+") в ("+str(step[2])+";"+str(step[3])+")")
            #print(color+" перемещаеться из ("+str(step[0])+";"+str(step[1])+") в ("+str(step[2])+";"+str(step[3])+")")
    change_square(board)
    if e==0:
        next_player()
    if op[4]!=1:
        render()
    
def SAI2(color):
    e=0
    board=square
    steps=find_all_available_moves(color,board)
    step=calculate_Best_Move(color,board,steps)
    board=final_move_on_board(step[0],step[1],step[2],step[3],step[4],board)
    if step[4]==True:
        steps=find_select_step_in_steps(step[2],step[3],find_all_steps(color,board),True)
        if len(steps)>0:
            e=1
            #print(color+" бъет другую шашку и перемещаеться из ("+str(step[0])+";"+str(step[1])+") в ("+str(step[2])+";"+str(step[3])+")")
            #print(color+" перемещаеться из ("+str(step[0])+";"+str(step[1])+") в ("+str(step[2])+";"+str(step[3])+")")
    
    change_square(board)
    if e==0:
        if color=="black":
            Player[0]=2
        else:
            Player[0]=1
    if op[4]!=1:
        render()
    
def SAI(color):
    e=0
    board=square
    steps=find_all_available_moves(color,board)
    step=calculate_Best_Move_for_one(color,board,steps)
    board=final_move_on_board(step[0],step[1],step[2],step[3],step[4],board)
    if step[4]==True:
        steps=find_select_step_in_steps(step[2],step[3],find_all_steps(color,board),True)
        if len(steps)>0:
            e=1
    change_square(board)
    if e==0:
        if color=="black":
            Player[0]=2
        else:
            Player[0]=1
    if op[4]!=1:
        render()
def AI(color):
    e=0
    board=square
    steps=find_all_available_moves(color,board)
    step=random.choice(steps)
    board=final_move_on_board(step[0],step[1],step[2],step[3],step[4],board)
    if step[4]==True:
        steps=find_select_step_in_steps(step[2],step[3],find_all_steps(color,board),True)
        if len(steps)>0:
            e=1
    change_square(board)
    #print(color+" бъет другую шашку и перемещаеться из ("+str(step[0])+";"+str(step[1])+") в ("+str(step[2])+";"+str(step[3])+")")
    #print(step)
    #####
    change_square(board)
    if e==0:
        if color=="black":
            Player[0]=2
        else:
            Player[0]=1
    if op[4]!=1:
        render()
def move_on_board(x1,y1,x2,y2,eat,board):
    board[x2][y2]=board[x1][y1]
    board[x1][y1]=None
    if board[x2][y2].color=="white":
        if y2==7:
            board[x2][y2].gking()
    else:
        if y2==0:
            board[x2][y2].gking()
    if eat==True:
        board[x2-toone((x2-x1)//2)][y2-toone((y2-y1)//2)]=None
    return board
def final_move_on_board(x1,y1,x2,y2,eat,board):
    if op[4]==1:
        render()
        animation(x1,x2,y1,y2,eat)
    board[x2][y2]=board[x1][y1]
    board[x1][y1]=None
    if board[x2][y2].color=="white":
        if y2==7:
            board[x2][y2].gking()
    else:
        if y2==0:
            board[x2][y2].gking()
    if eat==True:
        board[x2-toone((x2-x1)//2)][y2-toone((y2-y1)//2)]=None
    return board
def calculateBoard(board,color):
    HM=0
    c=countofcolor_on_board(color,board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!=None:
                if board[i][j].color==color:
                    if board[i][j].king==False:
                        HM+=10
                    else:
                        HM+=20
                else:
                    if board[i][j].king==False:
                        HM-=10
                    else:
                        HM-=20
    return HM
def find_select_step_in_steps(x,y,steps,eat):
    if eat==True:
        return [i for i in steps if i[0]==x and i[1]==y and i[4]==True]
    else:
        return [i for i in steps if i[0]==x and i[1]==y]
def find_all_steps(color,board):
    steps=[]
    for sx in range(len(board)):
        for sy in range(len(board[sx])):
            if board[sx][sy]!=None: 
                if board[sx][sy].color==color:
                    d=[(1,1),(-1,1),(-1,-1),(1,-1)]
                    if board[sx][sy].king==False:
                        for i in range(4):
                            x=sx
                            y=sy
                            x+=d[i][0]
                            y+=d[i][1]
                            if 0<=x and x<8 and 0<=y and y<8:
                                if board[x][y]== None:
                                    if (board[sx][sy].color=="white" and i<2) or (board[sx][sy].color=="black" and i>=2):
                                            steps+=[(sx,sy,x,y,False)]
                                else:
                                    if board[sx][sy].color=="black":
                                        if board[x][y].color=="white":
                                            if 0<=x+x-sx and x+x-sx<8 and 0<=y+y-sy and y+y-sy<8:
                                                if board[x+x-sx][y+y-sy]==None:
                                                    steps+=[(sx,sy,x+x-sx,y+y-sy,True)]
                                    else:
                                        if board[x][y].color=="black":
                                            if 0<=x+x-sx and x+x-sx<8 and 0<=y+y-sy and y+y-sy<8:
                                                if board[x+x-sx][y+y-sy]==None:
                                                    steps+=[(sx,sy,x+x-sx,y+y-sy,True)]
                    else:
                        for i in range(4):
                            x=sx
                            y=sy
                            for j in range(8):
                                x+=d[i][0]
                                y+=d[i][1]
                                if 0<=x and x<8 and 0<=y and y<8:
                                    if board[x][y]== None:
                                        if Extra_turn[0]==0:
                                            steps+=[(sx,sy,x,y,False)]
                                    else:
                                        if board[sx][sy].color=="black":
                                            if board[x][y].color=="white":
                                                if 0<=x+d[i][0] and x+d[i][0]<8 and 0<=y+d[i][1] and y+d[i][1]<8:
                                                    if board[x+d[i][0]][y+d[i][1]]==None:
                                                        steps+=[(sx,sy,x+d[i][0],y+d[i][1],True)]
                                        else:
                                            if board[x][y].color=="black":
                                                if 0<=x+d[i][0] and x+d[i][0]<8 and 0<=y+d[i][1] and y+d[i][1]<8:
                                                    if board[x+d[i][0]][y+d[i][1]]==None:
                                                        steps+=[(sx,sy,x+d[i][0],y+d[i][1],True)]
                                        break
    return steps
def countofcolor_on_board(color,board):
    HM=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!=None: 
                if board[i][j].color==color:
                    HM+=1
    return HM
def countofcolor(color):
    HM=0
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j]!=None: 
                if square[i][j].color==color:
                    HM+=1
    return HM
def popup(event):
    if anime[0]==0:
        render()
        x = event.x
        y = event.y
        x=x//cell
        y=y//cell
        if op[1]==5 or op[2]==5:
            if Gsteps[0]!=[]:
                for i in Gsteps[0]:
                    if x==i[2] and y==i[3]:
                        move(Gselect[0][0][0],Gselect[0][0][1],i[2],i[3],i[4])
                        #выключить при анимации
                        if op[4]!=1:
                            render()
            if Extra_turn[0]==0 or (x==Extra_turn[1][0] and y==Extra_turn[1][1]):
                if find(x,y)==Player[0]:
                    #выключить при анимации
                    if op[4]!=1:
                        render()
                    c.create_rectangle(cell*x+1, cell*y+1, cell*x+cell,cell*y+cell,outline='red')
                    Gselect[0]=[(x,y)]
                    #добавил генерацию ходов для чёрных
                    if Player[0]==2:
                        steps=find_all_available_moves("white",square)
                    else:
                        steps=find_all_available_moves("black",square)
                    if Extra_turn[0]==0:
                        steps=find_select_step_in_steps(x,y,steps,False)
                        Gsteps[0]=steps
                    else:
                        steps=find_select_step_in_steps(x,y,steps,True)
                        Gsteps[0]=steps
                    for i in steps:
                        c.create_rectangle(cell*i[2]+1, cell*i[3]+1, cell*i[2]+cell,cell*i[3]+cell,outline='yellow')
                else:
                    Gsteps[0]=[]
                    Gselect[0]=[]

        if Player[0]==1:
            if countofcolor("black")>0:
                print("черные ходят")
                try:
                    if op[2]==1:
                        SAI2("black")
                    elif op[2]==2:
                        SAI3("black")
                    elif op[2]==3:
                        SAI("black")
                    elif op[2]==4:
                        AI("black")
                except:
                    print("черные не могут походить")
                pass
            else:
                print("белые выиграли")
        else:
            if countofcolor("white")>0:
                print("белые ходят")
                try:
                    if op[1]==1:
                        SAI2("white")
                    elif op[1]==2:
                        SAI3("white")
                    elif op[1]==3:
                        SAI("white")
                    elif op[1]==4:
                        AI("white")
                except:
                    print("белые не могут походить")
                pass
            else:
                print("черные выиграли")
def findobj(ch):
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j]==ch:
                return (i,j)
def toone(x):
    if x<0:
        return -1
    else:
        return 1
def animation(x1,x2,y1,y2,eat):
    anime[0]=1
    global square
    c.create_rectangle(x1*(sizefield//8)+1, y1*(sizefield//8)+1, (x1+1)*(sizefield//8), (y1+1)*(sizefield//8),fill='gray',outline='gray')
    if square[x1][y1].color=="white":
        ball = c.create_oval(x1*(sizefield//8)+1, y1*(sizefield//8)+1, (x1+1)*(sizefield//8), (y1+1)*(sizefield//8),fill='white',outline='black')
        if square[x1][y1].king==True:
            kingball=c.create_oval(x1*(sizefield//8)+cell//4, y1*(sizefield//8)+cell//4, (x1+1)*(sizefield//8)-cell//4, (y1+1)*(sizefield//8)-cell//4,fill='red',outline='black')
    else:
        ball = c.create_oval(x1*(sizefield//8)+1, y1*(sizefield//8)+1, (x1+1)*(sizefield//8), (y1+1)*(sizefield//8),fill='black',outline='white')
        if square[x1][y1].king==True:
            kingball=c.create_oval(x1*(sizefield//8)+cell//4, y1*(sizefield//8)+cell//4, (x1+1)*(sizefield//8)-cell//4, (y1+1)*(sizefield//8)-cell//4,fill='red',outline='white')
    def motion():
        if x2>x1 and y2>y1:
            try:
                c.move(kingball,1,1)
            except:
                pass
            c.move(ball, 1, 1)
            if c.coords(ball)[2] < x2*cell+cell:
                
                 window.after(10, motion)
            else:
                anime[0]=0
                if eat==True:
                    c.create_rectangle((x2-1)*(sizefield//8)+1, (y2-1)*(sizefield//8)+1, x2*(sizefield//8), y2*(sizefield//8),fill='gray',outline='gray')
        if x2<x1 and y2>y1:
            try:
                c.move(kingball,-1,1)
            except:
                pass
            c.move(ball, -1, 1)
            if c.coords(ball)[2] > x2*cell+cell:
                 window.after(10, motion)
            else:
                anime[0]=0
                if eat==True:
                    c.create_rectangle((x2+1)*(sizefield//8)+1, (y2-1)*(sizefield//8)+1, (x2+2)*(sizefield//8), y2*(sizefield//8),fill='gray',outline='gray')
        if x2<x1 and y2<y1:
            try:
                c.move(kingball,-1,-1)
            except:
                pass
            c.move(ball, -1, -1)
            if c.coords(ball)[2] > x2*cell+cell:
                 window.after(10, motion)
            else:
                anime[0]=0
                if eat==True:
                    c.create_rectangle((x2+1)*(sizefield//8)+1, (y2+1)*(sizefield//8)+1, (x2+2)*(sizefield//8), (y2+2)*(sizefield//8),fill='gray',outline='gray')
        if x2>x1 and y2<y1:
            try:
                c.move(kingball,1,-1)
            except:
                pass
            c.move(ball, 1, -1)
            if c.coords(ball)[2] < x2*cell+cell:
                 window.after(10, motion)
            else:
                anime[0]=0
                if eat==True:
                    c.create_rectangle((x2-1)*(sizefield//8)+1, (y2+1)*(sizefield//8)+1, x2*(sizefield//8), (y2+2)*(sizefield//8),fill='gray',outline='gray')
    motion()
def move(x1,y1,x2,y2,eat):
    #print(x1,y1,x2,y2)
    if eat==True:
        print(str(square[x1][y1].color)+" ест "+str(square[x2-toone((x2-x1)//2)][y2-toone((y2-y1)//2)].color)+" и перемещаеться из ("+str(x1)+";"+str(y1)+") в ("+str(x2)+";"+str(y2)+")")
    else:
        print(str(square[x1][y1].color)+" перемещаеться из ("+str(x1)+";"+str(y1)+") в ("+str(x2)+";"+str(y2)+")")
######тут будет анимация
    if op[4]==1:
        animation(x1,x2,y1,y2,eat)
    square[x2][y2]=square[x1][y1]
    square[x1][y1]=None
    if square[x2][y2].color=="white":
        if y2==7:
            square[x2][y2].gking()
    else:
        if y2==0:
            square[x2][y2].gking()
    if eat==True:
        square[x2-toone((x2-x1)//2)][y2-toone((y2-y1)//2)]=None
        if len([i for i in findsteps(x2,y2) if i[2]==True])>0:
            Extra_turn[1]=(x2,y2)
            Extra_turn[0]=1
            print("extra")
        else:
            Extra_turn[0]=0
            if Player[0]==2:
                Player[0]=1
                Eat[0]=eatHM("black")
            else:
                Player[0]=2
                Eat[0]=eatHM("white")
        
            
    else:
        Extra_turn[0]=0
        if Player[0]==2:
            Player[0]=1
            Eat[0]=eatHM("black")
        else:
            Player[0]=2
            Eat[0]=eatHM("white")
def find(x,y):
    if square[x][y]!= None:
        if square[x][y].color=="black":
            return 1
        else:
            return 2
    return 0
def eatHM(color):
    HM=0
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j]!=None: 
                if square[i][j].color==color:
                    HM+=len([i for i in findsteps(i,j)if i[2]==True])
    return HM
def findsteps(x,y):
    sx=x
    sy=y
    d=[(1,1),(-1,1),(-1,-1),(1,-1)]
    steps=[]
    if square[sx][sy].king==False:
        for i in range(4):
            x=sx
            y=sy
            x+=d[i][0]
            y+=d[i][1]
            if 0<=x and x<8 and 0<=y and y<8:
                if square[x][y]== None:
                    if (square[sx][sy].color=="white" and i<2) or (square[sx][sy].color=="black" and i>=2):
                        if Extra_turn[0]==0:
                            steps+=[(x,y,False)]
                else:
                    if square[sx][sy].color=="black":
                        if square[x][y].color=="white":
                            if 0<=x+x-sx and x+x-sx<8 and 0<=y+y-sy and y+y-sy<8:
                                if square[x+x-sx][y+y-sy]==None:
                                    steps+=[(x+x-sx,y+y-sy,True)]
                    else:
                        if square[x][y].color=="black":
                            if 0<=x+x-sx and x+x-sx<8 and 0<=y+y-sy and y+y-sy<8:
                                if square[x+x-sx][y+y-sy]==None:
                                    steps+=[(x+x-sx,y+y-sy,True)]
    else:
        for i in range(4):
            x=sx
            y=sy
            for j in range(8):
                x+=d[i][0]
                y+=d[i][1]
                if 0<=x and x<8 and 0<=y and y<8:
                    if square[x][y]== None:
                        if Extra_turn[0]==0:
                            steps+=[(x,y,False)]
                    else:
                        if square[sx][sy].color=="black":
                            if square[x][y].color=="white":
                                if 0<=x+d[i][0] and x+d[i][0]<8 and 0<=y+d[i][1] and y+d[i][1]<8:
                                    if square[x+d[i][0]][y+d[i][1]]==None:
                                        steps+=[(x+d[i][0],y+d[i][1],True)]
                        else:
                            if square[x][y].color=="black":
                                if 0<=x+d[i][0] and x+d[i][0]<8 and 0<=y+d[i][1] and y+d[i][1]<8:
                                    if square[x+d[i][0]][y+d[i][1]]==None:
                                        steps+=[(x+d[i][0],y+d[i][1],True)]
                        break
    esteps=[i for i in steps if i[2]==True]
    if Eat[0]>0:
        return esteps
    return steps
def render():
    for i in range(8):
        for j in range(8):
            if i%2==0:
                if j%2==0:
                    c.create_rectangle(i*(sizefield//8)+1, j*(sizefield//8)+1, (i+1)*(sizefield//8), (j+1)*(sizefield//8),fill='gray',outline='gray')
                else:
                    c.create_rectangle(i*(sizefield//8)+1, j*(sizefield//8)+1, (i+1)*(sizefield//8), (j+1)*(sizefield//8),fill='white',outline='white')
            else:
                if j%2==0:
                    c.create_rectangle(i*(sizefield//8)+1, j*(sizefield//8)+1, (i+1)*(sizefield//8), (j+1)*(sizefield//8),fill='white',outline='white')
                else:
                    c.create_rectangle(i*(sizefield//8)+1, j*(sizefield//8)+1, (i+1)*(sizefield//8), (j+1)*(sizefield//8),fill='gray',outline='gray')
    for i in range(len(square)):
        for j in range(len(square[j])):
            if square[i][j] !=None:
                if square[i][j].color=="white":
                    c.create_oval(i*(sizefield//8)+1, j*(sizefield//8)+1, (i+1)*(sizefield//8), (j+1)*(sizefield//8),fill='white',outline='black')
                    if square[i][j].king==True:
                        c.create_oval(i*(sizefield//8)+cell//4, j*(sizefield//8)+cell//4, (i+1)*(sizefield//8)-cell//4, (j+1)*(sizefield//8)-cell//4,fill='red',outline='black')
                else:
                    c.create_oval(i*(sizefield//8)+1, j*(sizefield//8)+1, (i+1)*(sizefield//8), (j+1)*(sizefield//8),fill='black',outline='white')
                    if square[i][j].king==True:
                        c.create_oval(i*(sizefield//8)+cell//4, j*(sizefield//8)+cell//4, (i+1)*(sizefield//8)-cell//4, (j+1)*(sizefield//8)-cell//4,fill='red',outline='white')
x = 0
y = 0
def popup2(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)
def create_white():
    sx=x//cell
    sy=y//cell
    square[sx][sy]=checkers("white")
    render()
def create_black():
    sx=x//cell
    sy=y//cell
    square[sx][sy]=checkers("black")
    render()
def delite_checkers():
    sx=x//cell
    sy=y//cell
    square[sx][sy]=None
    render()
def make_king():
    sx=x//cell
    sy=y//cell
    if square[sx][sy]!=None:
        square[sx][sy].gking()
    render()
def next_player():
    if Player[0]==2:
        Player[0]=1
    else:
        Player[0]=2
def save_square():
    save_and_load_board[0]=Player[0]
    save_and_load_board[1]=copyofboard(square)
def load_square():
    Player[0]=save_and_load_board[0]
    change_square(save_and_load_board[1])
    save_square()
    render()
def clear_square():
    change_square([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]])
    render()
global op
op=[1,5,5,0,0,400]
def apply_options():
    global op
    op=local_op[:]
    remenu()
    opt.destroy()
    print(op)
    print(group7.get())
def op0():
    if local_op[0]==1:
        local_op[0]=0
    else:
        local_op[0]=1
    print(op,local_op)
def op4():
    if local_op[4]==1:
        local_op[4]=0
    else:
        local_op[4]=1
    print(op,local_op)
#Начало блока rd_command
def rd1_command():
    local_op[1]=1
def rd2_command():
    local_op[1]=2
def rd3_command():
    local_op[1]=3
def rd4_command():
    local_op[1]=4
def rd5_command():
    local_op[1]=5
def rd6_command():
    local_op[2]=1
def rd7_command():
    local_op[2]=2
def rd8_command():
    local_op[2]=3
def rd9_command():
    local_op[2]=4
def rd10_command():
    local_op[2]=5
#Конец блока rd_command
def op3():
    if local_op[3]==1:
        local_op[3]=0
    else:
        local_op[3]=1
def options():
    global opt,local_op,group7
    local_op=op[:]
    try:
        opt.destroy()
    except:
        pass
    group1=IntVar()
    group2=IntVar()
    group3=IntVar()
    group4=IntVar()
    group5=IntVar()
    group6=IntVar()
    group7=IntVar()
    opt=Tk()
    opt.title("Настройки")
    sandbox=Checkbutton(opt,text="Sandbox",variable=group3,command=op0)
    save=Checkbutton(opt,text="Сохранение",variable=group4,command=op3)
    log=Checkbutton(opt,text="Лог",variable=group5)
    anim=Checkbutton(opt,text="Анимация (Тестовая версия)",variable=group6,command=op4)
    sandbox.grid(row=0,column=0,sticky="w")
    save.grid(row=0,column=1,sticky="w")
    anim.grid(row=1,column=0,sticky="w",columnspan=2)
    l1=Label(opt,text="Белые:")
    l2=Label(opt,text="Чёрные:")
    rb1=Radiobutton(opt,text='Сильный ИИ',variable=group2,value=1,command=rd1_command)
    rb2=Radiobutton(opt,text='Средний ИИ',variable=group2,value=2,command=rd2_command)
    rb3=Radiobutton(opt,text='Слабый ИИ',variable=group2,value=3,command=rd3_command)
    rb4=Radiobutton(opt,text='Рандом',variable=group2,value=4,command=rd4_command)
    rb5=Radiobutton(opt,text='Игрок',variable=group2,value=5,command=rd5_command)
    rb6=Radiobutton(opt,text='Сильный ИИ',variable=group1,value=1,command=rd6_command)
    rb7=Radiobutton(opt,text='Средний ИИ',variable=group1,value=2,command=rd7_command)
    rb8=Radiobutton(opt,text='Слабый ИИ',variable=group1,value=3,command=rd8_command)
    rb9=Radiobutton(opt,text='Рандом',variable=group1,value=4,command=rd9_command)
    rb10=Radiobutton(opt,text='Игрок',variable=group1,value=5,command=rd10_command)
    apply=Button(opt,text="Применить настройки",command=apply_options)
    l1.grid(row=2,column=0,sticky="w")
    l2.grid(row=2,column=1,sticky="w")
    rb1.grid(row=3,column=0,sticky="w")
    rb2.grid(row=4,column=0,sticky="w")
    rb3.grid(row=5,column=0,sticky="w")
    rb4.grid(row=6,column=0,sticky="w")
    rb5.grid(row=7,column=0,sticky="w")
    rb6.grid(row=3,column=1,sticky="w")
    rb7.grid(row=4,column=1,sticky="w")
    rb8.grid(row=5,column=1,sticky="w")
    rb9.grid(row=6,column=1,sticky="w")
    rb10.grid(row=7,column=1,sticky="w")

    apply.grid(row=9,columnspan=2)
    if local_op[0]==1:
        sandbox.select()
    if local_op[3]==1:
        save.select()
    if local_op[1]==1:
        rb1.select()
    elif local_op[1]==2:
        rb2.select()
    elif local_op[1]==3:
        rb3.select()
    elif local_op[1]==4:
        rb4.select()
    elif local_op[1]==5:
        rb5.select()
    if local_op[2]==1:
        rb6.select()
    elif local_op[2]==2:
        rb7.select()
    elif local_op[2]==3:
        rb8.select()
    elif local_op[2]==4:
        rb9.select()
    elif local_op[2]==5:
        rb10.select()
    if op[4]==1:
        anim.select()
    opt.mainloop()
def remenu():
    global menu
    try:
        del menu
    except NameError:
        pass
    menu = Menu(tearoff=0)
    if op[0]==1:
        menu.add_command(label="Создать белую", command=create_white)
        menu.add_command(label="Создать черную", command=create_black)
        menu.add_command(label="Удалить", command=delite_checkers)
        menu.add_command(label="Сделать дамкой", command=make_king)
        menu.add_command(label="Передать ход", command=next_player)
        menu.add_command(label="Очистить", command=clear_square)
    if op[3]==1:
        menu.add_command(label="Сохранить", command=save_square)
        menu.add_command(label="Загрузить", command=load_square)
    menu.add_command(label="Настройки", command=options)
for j in range(4):
    square[2*j]+=[checkers("white")]
    square[2*j]+=[None]
    square[2*j]+=[checkers("white")]
    square[2*j]+=[None]
    square[2*j]+=[None]
    square[2*j]+=[None]
    square[2*j]+=[checkers("black")]
    square[2*j]+=[None]
    square[2*j+1]+=[None]
    square[2*j+1]+=[checkers("white")]
    square[2*j+1]+=[None]
    square[2*j+1]+=[None]
    square[2*j+1]+=[None]
    square[2*j+1]+=[checkers("black")]
    square[2*j+1]+=[None]
    square[2*j+1]+=[checkers("black")]
save_square()
sizefield=400
cell=int(sizefield/8)
window = Tk()
window.title('Шашки')
c = Canvas(width=sizefield, height=sizefield, bg='white')
c.pack()
c.bind("<Button-1>", popup)
c.bind("<Button-3>", popup2)
remenu()
render()
window.mainloop()
print(calculateBoard(square,"white"))
