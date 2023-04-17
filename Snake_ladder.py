# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:54:21 2022

@author: Alok kumar
"""
from PIL import Image
import random
def show_board():
    img = Image.open("snake_ladder.jpg")
    img.show()
def play():
    ladder = {}
    snake = {}
    ladder[4] = 14
    ladder[8] = 30
    ladder[28] = 77
    ladder[21] = 42
    ladder[50] = 67
    ladder[71] = 92
    ladder[80] = 98
    snake[32] = 10
    snake[36] = 6
    snake[48] = 26
    snake[62] = 18
    snake[88] = 24
    snake[95] = 56
    snake[99] = 78
    scr1=0
    scr2=0
    turn=0
    ply1 = input("player1 enter your name \n")
    ply2 = input("player2 enter your name \n")
    while(1):
        if turn%2==0:
            print(ply1, " Your turn")
            print(scr1)
            dice = random.randint(1, 6)
            print("show on dice ",dice)
            scr1 = scr1+dice
            if scr1>100:
                scr1=scr1-dice
            if scr1 in ladder:
                scr1 = ladder[scr1]
            else:
                if scr1 in snake:
                    scr1 = snake[scr1]
            if(scr1==100):
                print(ply1, " Won")
                break
            ch = input("do you want to continue y/n? \n")
            if ch == 'n':
                break
                
            
            
        else:
            print(ply2," Your turn")
            print(scr2)
            dice = random.randint(1, 6)
            print("show on dice ",dice)
            scr2 = scr2+dice
            if scr2>100:
                scr2 = scr2-dice
            if scr2 in ladder:
                scr2 = ladder[scr2]
            else:
                if scr2 in snake:
                    scr2 = snake[scr2]
            if(scr2==100):
                print(ply2, " Won")
                break
            ch = input("do you want to continue y/n? \n")
            if ch == 'n':
                break
        turn = turn+1
       
show_board()
play()


