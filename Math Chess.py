import pygame, sys
import re
import sys
import os
import json
from tkinter import *
from pygame.locals import *
import time
from socket import *
import threading
import json
import ast
import inspect
import ctypes
"""---------Global Defining---------"""
WindowHeight    =   750   #WINDOW SIZE
WindowWidth     =   1200
C_size          =   35    #CHESS SIZE
CircleSize      =   30    
Gap             =   3     #Gap BETWEEN CHESS
LTMARGIN        =   int((WindowWidth-(C_size+Gap)*28)/2)
TOPMARGIN       =   int((WindowHeight-(C_size+Gap)*18)/2)
#COLORS                 R   G   B
Dark           =   (   0,  0,  0)
Light_Blue       =   (  40,191,255)
Light_Blue2      =   (   0,  0,255)
LtYellow     =   ( 255,225,  0)
White           =   ( 255,255,255)
Red             =   ( 255,  0,  0)
Blue            =   (   0,  0,255)
Crimson         =   ( 220, 20, 60)
LightPink       =   ( 255,182,193)
DeepSkyBlue     =   (   0,191,255)
#COLORS END
Screen     =   pygame.display.set_mode((WindowWidth,WindowHeight))   #WINDIW DISPLAYED
working = True
backGround      =   pygame.image.load("background.png")
firstChess      =   None      #FIRST CHESS CHOSEN
midChess        =   None      #CHESS IN THE MIDDLE
currentChess    =   None      #CHESS CURRENTLY CHOSEN
index           =   0         #NUMBERS OF CHESS
#GRID DEFINING
CBoard        =   {                      # 编号：【列，行，棋子编号】
        
        
        
                                                                            29:[7,0,0],
                                                                    22:[6,1,0],
                                                        16:[5,2,0],         30:[7,2,0],
                                                11:[4,3,0],         23:[6,3,0],
                                    5:[3,4,5],          17:[5,4,0],         31:[7,4,0],
                            6:[2,5,6],          12:[4,5,0],         24:[6,5,0],
                10:[1,6,10],        4:[3,6,3],          18:[5,6,0],         32:[7,6,0],
        1:[0,7,1],          7:[2,7,7],          13:[4,7,0],         25:[6,7,0],
                9:[1,8,9],          3:[3,8,4],          19:[5,8,0],         33:[7,8,0],
                            8:[2,9,8],          14:[4,9,0],         26:[6,9,0],
                                    2:[3,10,2],         20:[5,10,0],        34:[7,10,0],
                                                15:[4,11,0],        27:[6,11,0],
                                                        21:[5,12,0],        35:[7,12,0],
                                                                    28:[6,13,0],
                                                                            36:[7,14,0],
        37:[8,1,0],
                    44:[9,2,0],
        38:[8,3,0],          50:[10,3,0],
                    45:[9,4,0],             55:[11,4,12],
        39:[8,5,0],          51:[10,5,0],               61:[12,5,18],
                    46:[9,6,0],             56:[11,6,14],           62:[13,6,19],
        40:[8,7,0],          52:[10,7,0],               60:[12,7,17],       64:[14,7,11],
                    47:[9,8,0],             57:[11,8,13],           63:[13,8,20],
        41:[8,9,0],          53:[10,9,0],               59:[12,9,16],
                    48:[9,10,0],            58:[11,10,15],
        42:[8,11,0],         54:[10,11,0],
                    49:[9,12,0],
        43:[8,13,0],         
                    }
"""---------GLOBAL DEFINING END---------"""

def RestartProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
"""---------GRID DRAWING---------"""
def GridDrawing(order):
    
    Screen.blit(backGround,(0,0)) 
    LineDrawing_L()
    LineDrawing_R()
    CircleDrawing()
    color4 = (100, 100, 100)
    pygame.draw.rect(Screen, color4, [1000, 20, 100, 30], 3)
    pygame.draw.rect(Screen, color4, [90, 20, 100, 30], 3)
    font1 = pygame.font.Font('C:\Windows\Fonts\STXINGKA.TTF', 20)
    font2 = pygame.font.Font('C:\Windows\Fonts\STXINGKA.TTF', 30)
    note1 = font1.render("得分", True, Red)
    note2 = font1.render("得分", True, Blue)
    note3 = font2.render("叫停", True, Red)
    note4 = font2.render("叫停", True, Blue)
    note5 = font2.render("悔棋", True, Red)
    note6 = font2.render("认输", True, Red)
    note7 = font2.render("悔棋", True, Blue)
    note8 = font2.render("认输", True, Blue)

    Screen.blit(note1, (1020, 130))
    Screen.blit(note2, (110, 130))
    Screen.blit(note3, (1010, 20))
    Screen.blit(note4, (100, 20))
    
    Screen.blit(note5, (1030, 500))
    Screen.blit(note6, (1030, 550))
    Screen.blit(note7, (70, 500))
    Screen.blit(note8, (70, 550))
   

   
    Scoring(my_Scoring(),his_Scoring())
    my_font = pygame.font.Font('C:\Windows\Fonts\STXINGKA.TTF', 30)

    if order==1:
        note6 = my_font.render("红方回合", True, Red)
        
        Screen.blit(note6, (700, 600))
        
    else:
        note5 = my_font.render("蓝方回合", True, Blue)
        Screen.blit(note5, (300, 600))

def LineDrawing_L(ind=0,ynd=7):    #DRAW LINE AT LEFT PART OF GRID
    x1,y1=IndexToXY(ind,ynd)
    x2,y2=IndexToXY(ind+1,ynd+1)
    x3,y3=IndexToXY(ind+1,ynd-1)
    pygame.draw.circle(Screen, (0,0,0),(x1+int(C_size/2),y1+int(C_size/2)), 13,2)       #(surface,colour,圆心,半径,填充粗细)    #左顶角
    pygame.draw.circle(Screen, (0,0,0),(x2+int(C_size/2),y2+int(C_size/2)), 13,2)       #(surface,colour,圆心,半径,填充粗细)    #中间
    pygame.draw.circle(Screen, (0,0,0),(x3+int(C_size/2),y3+int(C_size/2)), 13,2)                                              #中间

    pygame.draw.line(Screen,Dark,(x1+int(C_size/2),y1+int(C_size/2)),(x2+int(C_size/2),y2+int(C_size/2)),5)  #(surface,colour,起点,终点,线段粗细)
    pygame.draw.line(Screen,Dark,(x1+int(C_size/2),y1+int(C_size/2)),(x3+int(C_size/2),y3+int(C_size/2)),5)
    pygame.draw.line(Screen,Dark,(x2+int(C_size/2),y2+int(C_size/2)),(x3+int(C_size/2),y3+int(C_size/2)),5)   #(surface,colour,起点,终点,线段粗细)
    ind=ind+1
    if(ind==7):
        return 
    LineDrawing_L(ind,ynd+1)
    LineDrawing_L(ind,ynd-1)
    
def LineDrawing_R(ind=14,ynd=7):   #DRAW GRID AT RIGHT
    x1,y1=IndexToXY(ind,ynd)
    x2,y2=IndexToXY(ind-1,ynd+1)
    x3,y3=IndexToXY(ind-1,ynd-1)
    pygame.draw.circle(Screen, (0,0,0),(x1+int(C_size/2),y1+int(C_size/2)), 13,2)
    pygame.draw.line(Screen,Dark,(x1+int(C_size/2),y1+int(C_size/2)),(x2+int(C_size/2),y2+int(C_size/2)),5)
    pygame.draw.line(Screen,Dark,(x1+int(C_size/2),y1+int(C_size/2)),(x3+int(C_size/2),y3+int(C_size/2)),5)
    pygame.draw.line(Screen,Dark,(x2+int(C_size/2),y2+int(C_size/2)),(x3+int(C_size/2),y3+int(C_size/2)),5)
    ind=ind-1
    if(ind==7):
        return 
    LineDrawing_R(ind,ynd+1)
    LineDrawing_R(ind,ynd-1)
    
def CircleDrawing():                #画底板圆圈  蓝圈，白圈，红圈
    basicFont = pygame.font.Font(None, 24)
    for i in range(1,65):
        x=CBoard[i][0]
        y=CBoard[i][1]
        x1, y1 = IndexToXY(CBoard[i][0], CBoard[i][1])
        
        #蓝
        if i <= 10:   
            pygame.draw.circle(Screen,DeepSkyBlue,(LTMARGIN+2*x*(C_size+Gap),TOPMARGIN+y*(C_size+Gap)),int(CircleSize/2)-3,0)
            k=str((i-1)%10)
            Screen.blit(basicFont.render(k, True, Dark),(x1+C_size/3,y1+C_size/3-1))

        #白
        elif i>10 and i<55: 
            pygame.draw.circle(Screen, White,(LTMARGIN + 2 * x * (C_size + Gap), TOPMARGIN + y * (C_size + Gap)),int(CircleSize / 2) - 3, 0)
        
        #红
        else:
            pygame.draw.circle(Screen, (227,174,174),(LTMARGIN + 2 * x * (C_size + Gap), TOPMARGIN + y * (C_size + Gap)),int(CircleSize / 2) - 3, 0)
            if i==64:
                Screen.blit(basicFont.render("0", True, Dark), (x1 + C_size / 3, y1 + C_size / 3-1))
            else:
                k = str(i-54)
                Screen.blit(basicFont.render(k, True, Dark), (x1 + C_size / 3, y1 + C_size / 3-1))
"""---------GRID DRAWING END---------"""

"""---------CHESS DRAWING---------"""
def ChessDrawing():                             #画64个格子
    basicFont = pygame.font.Font(None, 24)
    for i in range(1,65):
       if CBoard[i][2]>0:
            x=CBoard[i][0]
            y=CBoard[i][1]
            if CBoard[i][2]<=10:
                pygame.draw.circle(Screen,Light_Blue,(LTMARGIN+2*x*(C_size+Gap),TOPMARGIN+y*(C_size+Gap)),int(C_size/2),0)
                pygame.draw.circle(Screen,Light_Blue2,(LTMARGIN+2*x*(C_size+Gap),TOPMARGIN+y*(C_size+Gap)),int(C_size/2)-3,0)
            else:
                pygame.draw.circle(Screen, LightPink,(LTMARGIN + 2 * x * (C_size + Gap), TOPMARGIN + y * (C_size + Gap)),int(C_size / 2), 0)
                pygame.draw.circle(Screen, Crimson,(LTMARGIN + 2 * x * (C_size + Gap), TOPMARGIN + y * (C_size + Gap)),int(C_size / 2) - 3,0)
            q = str((CBoard[i][2]-1)%10)
            Screen.blit(basicFont.render(q, True, Dark), (LTMARGIN+2*x*(C_size+Gap)-6,TOPMARGIN+y*(C_size+Gap)-7))

def SideDrawing(x,y):  #ADD A RING TO THE CHOSEN CHESS          #选中状态
    pygame.draw.circle(Screen,LtYellow,(x+int(C_size/2),y+int(C_size/2)),int(C_size/2)+3,3)

def IndexToXY(chessX,chessY):  #COODNINANCE OF CHESS
    left=LTMARGIN+2*chessX*(C_size+Gap)-int(C_size/2)
    top=TOPMARGIN+chessY*(C_size+Gap)-int(C_size/2)
    return(left,top)

def XYToIndex(x,y): #CONVERT COODNINANCE TO INDEX    #将棋子坐标转化为编号 
    for i in range(1,65):
        left,top=IndexToXY(CBoard[i][0],CBoard[i][1])
        chessRect=pygame.Rect(left,top,C_size,C_size)
        if chessRect.collidepoint(x,y):
            return(i)
    return(None)
"""---------CHESS DRAWING END---------"""

"""---------CHESS MOVING---------"""
def ChessJumping(firstChess,currentChess):#JUMP   如果可以跳，改变棋子分布，并返回True
    
    

    if IsGo(firstChess,currentChess):
        CBoard[currentChess][2] = CBoard[firstChess][2]    #将棋盘坐标上的‘是否为初始位置的棋子’状态改变，代表下棋后新的棋子分布
        CBoard[firstChess][2]=0

        pygame.mixer.init()
        sound = pygame.mixer.Sound('aaa.wav')
        sound.play(0,0)
 
        return True
    else:
        return False
 
def ChessJumping_back(firstChess,currentChess):# JUMP BACK
    CBoard[currentChess][2] = CBoard[firstChess][2]
    CBoard[firstChess][2]=0
        
def IsGo(firstChess,goalChess):
    if IsMove(firstChess,goalChess) or IsLinMove(firstChess,goalChess) or IsDanKua(firstChess,goalChess):
        return True
    
    return False

def IsMove(firstChess,goalChess):    #检测是否可以进行“移”操作
    if ifNeibor(firstChess,goalChess) and CBoard[firstChess][2]>0 and CBoard[goalChess][2]==0:
        return True
    return False

def IsLinMove(firstChess,goalChess):##检测是否可以进行“邻”操作
    x=abs(CBoard[firstChess][0]-CBoard[goalChess][0])
    y=abs(CBoard[firstChess][1]-CBoard[goalChess][1])
    x1=CBoard[firstChess][0]+CBoard[goalChess][0]
    y1=CBoard[firstChess][1]+CBoard[goalChess][1]
    if (x==y and x==2)or (x==0 and y==4):
        x2,y2=IndexToXY(x1/2,y1/2)
        z1=XYToIndex(x2,y2)
        if CBoard[z1][2]>0:
            return True#
    return False

def if_Central(firstChess, goalChess):
    x1 = abs(CBoard[firstChess][0] - 7)
    x2 = abs(CBoard[goalChess][0] - 7)
    if x2 < x1:
        return True
    return False

def if_Jumpable(firstChess,goalChess):
    a = []
    for chess in CBoard:
        if if_In_Line(firstChess, chess) and CBoard[chess][2] != 0:
            for chessb in CBoard:
                if if_In_Line(firstChess, chessb) and CBoard[chess][2] == 0:
                    x=abs(CBoard[chess][0]-CBoard[chessb][0])
                    y=abs(CBoard[chess][1]-CBoard[chessb][1])
                    if(x == y and x == 1):
                        if(if_Central(chess,chessb)):
                            a.append(chessb)


    if goalChess in a:
        return True
    return False

def IsDanKua(firstChess,goalChess):#检测是否可以进行“单跨”操作   # 编号：【列，行，棋子编号】
    if if_Jumpable(firstChess,goalChess):
       return False

    m=CBoard[firstChess][0]-CBoard[goalChess][0]            #路差
    n=CBoard[firstChess][1]-CBoard[goalChess][1]            #行差
    u=abs(m)
    v=abs(n)
    if u != 0:   #不在一路
        p=m/u
        q=n/u
    else:       #在一路
        p=0
        q=n/v*2
    rg=abs(CBoard[firstChess][1]-CBoard[goalChess][1])#NUMBER OF CHESS IN THE MIDDLE
    xx0=CBoard[goalChess][0]
    yy0=CBoard[goalChess][1]
    xx1,yy1=IndexToXY(xx0+p,yy0+q)
    zz0=XYToIndex(xx1,yy1)
    #|DECIDE LAST POSITION OF SUCH CHESS
    x=[]#EMPTY LIST, ADDING WEIGHTS 
    if u==0:
        rg=int(rg/2)#HALF OF Y2-Y1
    if if_In_Line(firstChess,goalChess):#IF IN THE SAME LINE
        for i in range(1,rg):
            x0=xx0+p
            y0=yy0+q
            xx0=x0
            yy0=y0
            xx,yy=IndexToXY(x0,y0)
            z=int(XYToIndex(xx,yy))
            if CBoard[z][2] != 0:
                if CBoard[z][2]<11:
                    tmp=CBoard[z][2]-1
                else:
                    tmp=CBoard[z][2]-11
                x+=[tmp]#ADD CHESS WISHES SO TO THE LIST
        if CBoard[zz0][2] > 0:
            root = Tk()
            root.minsize(200, 200)
            root.title("提示")

            if CBoard[firstChess][2]<11:
                tp=CBoard[firstChess][2]-1
            else:
                tp=CBoard[firstChess][2]-11
            sss = str(x)
            sss2=str(tp)
            Label(root, text="请输入四则运算表达式").pack()
            Label(root, text="只使用以下数字各一次：").pack()
            Label(root, text=sss).pack()
            Label(root, text="且结果为：").pack()
            Label(root, text=sss2).pack()
            l1 = Label(root, text="输入：")
            root.geometry("%dx%d+%d+%d" % (300, 100, WindowWidth /2, (WindowHeight) / 3))
            xls_text = StringVar()
            l1.pack()  # side CAN BE: LEFT  RTGHT TOP  BOTTOM
            xls = Entry(root, textvariable=xls_text)
            xls_text.set("")
            xls.pack()
            Button(root, text="确认", command=root.destroy).pack( expand=YES)
            #Button(root, text="CANCEL", command=root.destroy).pack(side=LEFT, expand=YES)

            root.mainloop()
            expression=xls_text.get()
            print(xls_text)
            expre=re.findall(r"\d+",expression)#CINVERT NUMBERS TO LIST
            expre=list(map(int,expre))#CONVERT NUMBERS TO INTERGER
            Flag1=Define_SameSet(expre,x)#NUMBERS MATCH WITH CHESS
            if tp==t_Result(expression):#RESULT MATCH WITH CHESS
                Flag2=True
            else:
                Flag2=False
            if Flag1 and Flag2 and CBoard[zz0][2]>0:
                return True
            if Flag2==False or Flag1==False:
                root3=Tk()
                root3.title("提示")
                Label(root3,text="不符合条件").pack()
                root3.geometry("%dx%d+%d+%d" % (300, 100, (WindowWidth ) / 2, (WindowHeight ) / 3))
                root3.mainloop()
    return False

def ifNeibor(firstChess,midChess):#CHECK WHETHER JUMPING TO A NEIGHBORING CIRCLE
    x=abs(CBoard[firstChess][0]-CBoard[midChess][0])
    y=abs(CBoard[firstChess][1]-CBoard[midChess][1])
    if x==y and x==1:
        return True
    elif CBoard[firstChess][0]==CBoard[midChess][0] and y==2:   #在同一路相邻
        return True
    return False

def if_In_Line(firstChess,midChess):#CHECK WHETHER CHESS IN THE LINE
    x=abs(CBoard[firstChess][0]-CBoard[midChess][0])
    y=abs(CBoard[firstChess][1]-CBoard[midChess][1])
    if x==y:
        return True
    elif CBoard[firstChess][0]==CBoard[midChess][0]:
        return True
    return False

def Define_SameSet(a=[],b=[]):
    a.sort()
    b.sort()
    if a==b:
        return True
    else:
        return False
    
class Calculator(object):
    def __init__(self):
        # OPERATORS
        self.operators = ['+', '-', '*', '/', '(', ')']
        # PRIORITY
        self.priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 3,
            ')': 3
        }

    def generate_postfix_expression(self, expression): #生成后缀表达式
        
        
        # REMOVE SPACE BAR
        expression = expression.replace(' ', '')
        # CREATE STACK
        # OERATOR STACK
        operator_stack = list()
        # SAID STACK CAN BE REPLACED WITH LIST
        expression_stack = list()
        for element in expression:
            # NUMBERS ENTER THE STACK DIRECTLY
            if element in self.operators:
                # IF STACK EMPTY OR IS (, ENTER DIRECTLY
                if not operator_stack:
                    operator_stack.append(element)
                else:
                    # IF ), STACK POP UNTIL (, AND OPERATORS EXCEPT ()ENTER THE EXPRESSION
                    if element == ')':
                        for top in operator_stack[::-1]:
                            if top != '(':
                                expression_stack.append(top)
                                operator_stack.pop()
                            else:
                                operator_stack.pop()
                                break
                    else:
                        for top in operator_stack[::-1]:
                            # IF TARGET ELEMENT BIGGER THAN TOP, ENTER DIRECTLY, OR TOP POP, ENTER EXPRESSION
                            # (POPS ONLY WHEN ) POPS OUT
                            if self.priority[top] >= self.priority[element] and top != '(':
                                expression_stack.append(top)
                                operator_stack.pop()
                            else:
                                operator_stack.append(element)
                                break
                        # IF ALL OPERATORS POP OUT 
                        # AND TARGET OPERATOR NEEDS TO ENTER STACK
                        if not operator_stack:
                            operator_stack.append(element)
            else:
                expression_stack.append(element)
        # IF OPERATORS LEFT, ADD INTO EXPRESSION
        for i in range(len(operator_stack)):
            expression_stack.append(operator_stack.pop())
        return expression_stack

    def calcaulate(self, expression):
        # GENERATE POSTFIX
        expression_result = self.generate_postfix_expression(expression)
        calcalate_stack = list() #USE list AS A STACK
        # TRAVERSING POSTFIX
        for element in expression_result:
            # IF NUMBER ENTER DIRECTLY
            # IF OPERATOR, POP 2 NUMBERS
            if element not in self.operators:
                calcalate_stack.append(element)
            else:
                number1 = calcalate_stack.pop()# OPERATOR 1
                number2 = calcalate_stack.pop()# OPERATOR 2
                result = self.operate(number1, number2, element) # RESULT = (OPERATOR1 OPERATES OPERATOR2)
                calcalate_stack.append(result) # RESULT ENTER THE STACK
        return calcalate_stack[0]

    def operate(self, number1, number2, operator):
        #计算结果
        
        number1 = int(number1)
        number2 = int(number2)
        if operator == '+':
            return number2 + number1
        if operator == '-':
            return number2 - number1
        if operator == '*':
            return number2 * number1
        if operator == '/':
            if number2 % number1 == 0:
                return number2 / number1
            else:
                return -1

def t_Result(expression):
    c = Calculator()
    try:
        expression_result = c.calcaulate(expression)
    except(BaseException):
        return -1
    return (expression_result)

def my_Scoring():
    tmp=0
    ans=0
    for i in range(1,11):
        if CBoard[i][2]>10:
            ans=(i-1)*(CBoard[i][2]-11)+tmp
            tmp=ans
    return ans

def his_Scoring():
    tmp=0
    s=0
    for i in range(55,65):
        if CBoard[i][2]<11 and CBoard[i][2]>0:
            if i==64:
                s+=0
            else:
                s=(i-54)*(CBoard[i][2]-1)+tmp
            tmp=s
    return s

def Scoring(a,b):
    my_font = pygame.font.SysFont("arial", 30)
    Screen.blit(my_font.render(str(a), True, Dark), (1030, 90))
    Screen.blit(my_font.render(str(b), True, Dark), (120, 90))

def beginInitPygame(order):

    pygame.init()
    pygame.display.set_caption("国际数棋")
    pygame.mixer.init()
    pygame.mixer.music.load("夜的钢琴曲5 - 文武贝.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1,0.0)
    GridDrawing(order)
    ChessDrawing()

def giveUp(mouse_x,mouse_y,working):           #认输
    if ((1030 < mouse_x < 1170 and 550 < mouse_y < 580) or  (70 < mouse_x < 210 and 550 < mouse_y < 580))and working==True:
        working=False   #不工作状态
    
def retract(mouse_x,mouse_y,goback_s,goback_e,order_stack):          #悔棋
    if ((1020 < mouse_x < 1180 and 500 < mouse_y < 530) or  (60 < mouse_x < 220 and 500 < mouse_y < 530))and working==True:# GO BACK
        if goback_s!=[] and goback_e!=[]:
            print(goback_s)
            print(goback_e)
            firstChess = goback_s.pop()
            currentChess = goback_e.pop()
            order = not order_stack.pop()
            ChessJumping_back(firstChess, currentChess)
        firstChess=None

        GridDrawing(order)
        ChessDrawing()
                
def chooseChess(index,order,firstChess,goback_s,goback_e,order_stack,mouse_x,mouse_y):  #点击选中棋子
    if index!=None and CBoard[index][2]>0:    #棋盘刷新/移动棋子           CBoard[index][2]>0 说明此处位置有初始棋子    
                
        firstChess=index
        x,y=IndexToXY(CBoard[index][0],CBoard[index][1])              #[列，行，是否是初始棋子]

        GridDrawing(order)
        ChessDrawing()
        SideDrawing(x,y)   
    elif index!=None and CBoard[index][2]==0 and firstChess!=None:    
        currentChess=index                                   #可能为悔棋做准备

                #蓝色方下棋；棋子为蓝色方的棋子；没有叫停
        if order==False and CBoard[firstChess][2]<11 and working==True: 
            j=ChessJumping(firstChess,currentChess)   #可以跳，返回True
            if j:
                        order=True                         #order：false->true  蓝色方->红色方
                        goback_s += [currentChess]    #悔棋栈？
                        goback_e += [firstChess]      #悔棋栈？
                        order_stack +=[order]         #悔棋栈？     

                #红色方下棋；棋子为红色方的棋子；没有叫停
        elif order==True and CBoard[firstChess][2]>10 and working==True:
            j=ChessJumping(firstChess,currentChess)
            if j:
                        order=False
                        goback_s += [currentChess]
                        goback_e += [firstChess]
                        order_stack +=[order]

        firstChess=None  #一个棋子下完，初始化firstchess

                #绘制棋盘底、网格、文本；绘制64个新的棋子
        GridDrawing(order)
        ChessDrawing()
            #悔棋
    retract(mouse_x,mouse_y,goback_s,goback_e,order_stack)
            
            #红色方或蓝色方叫停
    redorBlue_halt(mouse_x,mouse_y,working)
            
            #游戏结束
    gameOver(working)

def redorBlue_halt(mouse_x,mouse_y,working):        #某一方叫停
            #红色叫停            
            if 1000 < mouse_x < 1100 and 20 < mouse_y < 50 and working==True :  #Red PAUSE
                tanchuang = 0
                for i in range(1,11):
                    if CBoard[i][2]<=10 or CBoard[i][2]==0:
                       tanchuang=1
                if tanchuang==1:
                    root1 = Tk()
                    root1.title("注意")
                    Label(root1, text="未达成叫停请求的要求").pack()
                    root1.geometry("%dx%d+%d+%d" % (300, 100, (WindowWidth +26)/2 , (WindowHeight -100) / 2))
                    root1.mainloop()
                else:
                    working = False

            #蓝色叫停
            elif 90 < mouse_x < 190 and 20 < mouse_y < 50 and working==True:  #Blue PAUSE
                tanchuang = 0
                for i in range(55,65):
                    if CBoard[i][2]>10 or CBoard[i][2]==0:
                       tanchuang=1
                if tanchuang==1:
                    root1 = Tk()
                    root1.title("注意")
                    
                    Label(root1, text="未达成叫停请求的要求").pack()

                    size = '%dx%d+%d+%d' % (100, 100, (WindowWidth - 100) / 2, (WindowHeight - 100) / 2)
                    root1.geometry("%dx%d+%d+%d" %(300, 100, (WindowWidth + 26) / 2, (WindowHeight -100) / 2))
                    root1.mainloop()
                else:
                    working=False
            
def gameOver(working):
    if working==False:  #END
        root2=Tk()
        root2.minsize(300,200)
        Label(root2,text="游戏结束").pack()
        if my_Scoring()>his_Scoring():
            Label(root2,text="红方 胜").pack()
        elif my_Scoring()==his_Scoring():
            Label(root2,text="平局").pack()
        else:
            Label(root2,text="蓝方 胜").pack()
        root2.geometry("%dx%d+%d+%d" % (200, 200, (WindowWidth +50) / 2, (WindowHeight +50) / 2))
        Button(root2, text="再来一局", command=root2.destroy).pack(side=LEFT, expand=YES)
        Button(root2, text="放弃", command=quit).pack(side=LEFT, expand=YES)
        root2.mainloop()
        main()


"""-------------------------------------------------socket-------------------------------------------------------------"""

#发送加入游戏信息
def sendBeginMsg(clientSocket):
    playMsg = {'type':0,'msg':{'name':"Ruimin"}}
    packet = json.dumps(playMsg)
    clientSocket.send(packet.encode('utf-8'))

#发送棋子移动信息
def send_Move(clientSocket, id, side, num, start_position, end_position, expression):
    send_message = {
        "type":1,
        "msg":{
            "game_id":id,
            "side":side,

            "scr":
            {
                "x":start_position[1],    ##与约定的相反
                "y":start_position[0]
            },

            "dst":
            {
                "x":end_position[1],
                "y":end_position[0]
            },
            "exp":expression
        }
    }
    packet = json.dumps(send_message)
    print("**************************")
    print(packet)
    print("**************************")
    clientSocket.send(packet.encode('utf-8'))

#发送叫停信息
def send_Stop(clientSocket, game_id,side):
    send_message ={
        "type":2,
        "msg":
        {
            "request":"stop",
            "game.id":game_id,
            "side":side
        }
    }
    packet = json.dumps(send_message)
    clientSocket.send(packet.encode('utf-8'))
#发送退出信息
def send_Quit(clientSocket,game_id,side):
    send_message = {
            "type":2,
            "msg":{
                'request':"quit",
                'game_id':game_id,
                'side':side
            }
    }
    packet = json.dumps(send_message)
    clientSocket.send(packet.encode('utf-8'))

#发送举报信息
def send_Report(clientSocket,game_id,side):
    send_message = {
        'type':2,
        'msg':{
            'request':"report",
            'game_id':game_id,
            'side': side
        }
    }
    packet = json.dumps(send_message)
    clientSocket.send(packet.encode('utf-8'))

#发送反馈信息
def send_Feedback(clientSocket,side):
    send_message= {
        'type':3,
        'side':side
    }
    packet = json.dumps(send_message)
    clientSocket.send(packet.encode('utf-8'))

def send_Dankua(clientSocket, side, num, game_id):
    send_message = {
        'type': 4,
        'msg': {
            'game_id': game_id,
            'dankua': num,
            'side': side}
    }
    packet = json.dumps(send_message)
    clientSocket.send(packet.encode('utf-8'))

def send_Over(clientSocket, side, num, game_id):
    send_message = {
        'type': 4,
        'msg': {
            'game_id': game_id,
            'chaoshi': num,
            'side': side}
    }
    packet = json.dumps(send_message)
    clientSocket.send(packet.encode('utf-8'))

'''    # 举报蓝方
def jubao_blue():
    if blue_step > 10:
        for i in range(4, 11):
            for j in range(0, 4):
                if CBoard[i][j] > 0:
                    return True
    return False


# 举报红方
def jubao_red():
    if red_step > 10:
        for i in range(4, 11):
            for j in range(11, 15):
                if ChessList[i][j] > 0:
                    return True
    return False

'''
# 接收信息
mes = []
def recv(clientSocket):
    # 循环接收消息
    while True:
        receive_message, serverAddress = clientSocket.recvfrom(2048)
        sentence = receive_message.decode('utf-8')
        if sentence != "":
            data = json.loads(sentence)
            # data = ast.literal_eval(sentence)
            mes.append(data)
            # print("有一条来自",addr,"的消息")
            print("             " + str(data))


# serverSocket = socket(AF_INET, SOCK_STREAM)
IP = "192.168.8.129"
# 绑定端口

serverPort = 50005
"""
serverSocket.bind(("192.168.8.107", serverPort))
serverSocket.listen(10)
# 创建一个子线程，执行接收消息的方法"""


'''clientSocket = socket(AF_INET, SOCK_STREAM)
serverName = IP
clientSocket.connect((IP, serverPort))
t1 = threading.Thread(target=recv, args=(clientSocket,))
# 开启线程
t1.start()
# 开始匹配
pipei = 0
game_id = 0

side0 = -1,
timenum = 31  # 倒计时时间
total_time = 31

start_position = (-1, -1)

MoveList = []
order = 1
Font3 = pygame.font.Font("E:\\学习小结\\程序设计实践\\华文行楷.ttf", 30)
start_time = 0


temp = 0
now_time = 0
huiqi = 0'''
"""--------------------------------------------------socket---------------------------------------------------------------"""
def main():

    mouse_x = 0
    mouse_y = 0
    working = True    ##如果叫停，则停止操作，working变为false
    order=True      ##每一次跳跃后order改变，True为红色方
    goback_s = []
    goback_e = []
    order_stack = []
    Go_Back_Flag = 0    # GO BACK FLAG
    #Forfeit_Flag = 0     #FORFEIT FLAG

    #初始化Pygame
    beginInitPygame(order)
    
    while True:
        mouseClicked=False
        for event in pygame.event.get():
            if event.type==QUIT or  (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONUP:
                mouse_x,mouse_y=event.pos
                mouseClicked=True

        Go_Back_Flag    =   0
        if  mouseClicked==True:
            index=XYToIndex(mouse_x,mouse_y)               #屏幕 1200，750

            #认输
            giveUp(mouse_x,mouse_y,working)

            #点击选中棋子
            if index!=None and CBoard[index][2]>0:    #棋盘刷新/移动棋子           CBoard[index][2]>0 说明此处位置有初始棋子    
                
                firstChess=index
                x,y=IndexToXY(CBoard[index][0],CBoard[index][1])              #[列，行，是否是初始棋子]

                GridDrawing(order)
                ChessDrawing()
                SideDrawing(x,y)                #将棋子变为选中状态


            #选择落子位置
            #鼠标点击有效棋子；不是两端初始的棋子；棋子已选中,等待选中落点
            elif index!=None and CBoard[index][2]==0 and firstChess!=None:    
                currentChess=index                                   #可能为悔棋做准备

                #蓝色方下棋；棋子为蓝色方的棋子；没有叫停
                if order==False and CBoard[firstChess][2]<11 and working==True: 
                    j=ChessJumping(firstChess,currentChess)   #可以跳，返回True
                    if j:
                        order=True                         #order：false->true  蓝色方->红色方
                        goback_s += [currentChess]    #悔棋栈？
                        goback_e += [firstChess]      #悔棋栈？
                        order_stack +=[order]         #悔棋栈？     

                #红色方下棋；棋子为红色方的棋子；没有叫停
                elif order==True and CBoard[firstChess][2]>10 and working==True:
                    j=ChessJumping(firstChess,currentChess)
                    if j:
                        order=False
                        goback_s += [currentChess]
                        goback_e += [firstChess]
                        order_stack +=[order]

                firstChess=None  #一个棋子下完，初始化firstchess

                #绘制棋盘底、网格、文本；绘制64个新的棋子
                GridDrawing(order)
                ChessDrawing()
            #悔棋
            retract(mouse_x,mouse_y,goback_s,goback_e,order_stack)
            
            #红色方或蓝色方叫停
            redorBlue_halt(mouse_x,mouse_y,working)
            
            #游戏结束
            gameOver(working)

        #下一步棋的代码
        pygame.display.update()
if __name__=='__main__':
    main()