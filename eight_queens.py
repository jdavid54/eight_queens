#!/usr/bin/env python
# coding: utf-8

import numpy as np

def possible(x,y):
    for c in range(1,8):    # same column
        #print('sc',c)
        if x+c > 7: break
        if board[x+c][y] == 'Q': return False
    for c in range(1,y+1):    # diagonal upleft
        #print('dul',c)
        if x-c < 0 or y-c < 0: break
        if board[x-c][y-c] == 'Q': return False
    for c in range(1,y+1):    # diagonal down left
        #print('ddl',c)
        if y-c < 0 or x+c > 7: break
        if board[x+c][y-c] == 'Q': return False
    for c in range(1,y+1):    # same row left
        #print('srl',c)
        if y-c < 0 : break
        if board[x][y-c] == 'Q': return False
    return True

possible(6,5)

def solve():
    global board
    
    #print(board)
    #r = input('halt')
    for y in range(8):       #columns
        success = False
        for x in range(8):   #rows            
            #if board[x][y]=='Q': break  
            print('yx=',y,x,board[x][y])
            if possible(x,y) : 
                success = True
                print('\t',x,y,success)
                #r = input('halt')
                #solve()
                board[x][y]='Q'
                #break
                solve()
                break
            #else: 
                #board[x][y]=' ' 
                #return
        if not success : return
    #solve(y+1)    
    #print('end at',x,y)    
    #solve()
    #board[x][y]=' '       
    return        


# In[145]:


# echiquier 8x8 cases
def init():
    board = [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ']]     
    return board


board = init()
solve()
board

solve()

board

