#!/usr/bin/env python
# coding: utf-8
import sys
import numpy as np
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

def possible(x,y):
    board[x][y] = '*'
    for c in range(0,8):    # same column
        #print('sc',c)        
        if x+c > 7: break
        if board[c][y] == 'Q': return False
        board[x+c][y] = ' ' #1
    for c in range(1,y+1):    # diagonal upleft
        #print('dul',c)
        
        if x-c < 0 or y-c < 0: break
        if board[x-c][y-c] == 'Q': return False
        board[x-c][y-c] = ' '
    for c in range(1,y+1):    # diagonal down left
        #print('ddl',c)
        
        if y-c < 0 or x+c > 7: break
        if board[x+c][y-c] == 'Q': return False
        board[x+c][y-c] = ' '
    for c in range(1,y+1):    # same row left
        #print('srl',c)        
        if y-c < 0 : break
        if board[x][y-c] == 'Q': return False
        board[x][y-c] = ' '
    return True

board = init()
def test():
    for c in range(8):    
        for r in range(8):        
            test = possible(r,c)
            if test: board[r][c]='Q'; break            
        print(r,c,test)
        for i in board:
            print(i)
        if not test : print('impossible'); sys.exit()
#test()        
def show():
    for i in board:
            print(i)
            
def solve(col):
    global board
    show()
    input('solve called'+str(col))
    for c in range(col,8):    
        for r in range(8):        
            test = possible(r,c)
            if test:
                board[r][c]='Q';
                #show()
                break
        if not test : print('impossible'); return
        solve(col+1)
        board[r][c]=' ';
        print(r,c,test)
        show()
        input('wtf?')
        return

solve(0)


'''
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

'''