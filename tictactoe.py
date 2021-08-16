import numpy as np
import pandas as pd
from tqdm import tqdm

class TicTacToe:
    def __init__(self,verbose=True,size = 3):
        self.__verbose=verbose
        self.__board = np.zeros((size,size),dtype=int)
        self.__size = size
        self.__move_num=0
        self.__current_turn=1

    def display(self,_return = False):

        if _return: return_string = ''
        for row in range(self.__size):
            line=''
            for elem in range(self.__size):
                line+=str(int(self.__board[row][elem]))
                if elem<self.__size-1:
                    line+='|'
            if _return:
                return_string+=line+'\n'
            else:
                print(line)
        if _return: return return_string

    def move(self,player,position):
        #check move is legal
        assert position[0]<self.__size, 'ERROR: position [{}][{}] is off of the board'.format(str(position[0]),str(position[1]))
        assert position[1]<self.__size, 'ERROR: position [{}][{}] is off of the board'.format(str(position[0]),str(position[1]))
        assert self.__board[position[0]][position[1]] == 0, 'ERROR: position [{}][{}] is already occupied by player {}'.format(str(position[0]),str(position[1]), str(self.__board[position[0]][position[1]]))
        
        #update values
        self.__board[position[0]][position[1]] = player
        self.__move_num +=1
        self.__current_turn = self.__current_turn=((self.__current_turn-2)%2)+1
        return self.__check_state()

    def __check_state(self):

        #check vertical and horiz lines
        for i in range(self.__size):
            if np.all(self.__board[0,i]==self.__board[:,i]) and self.__board[0,i] != 0: 

                return self.__board[0,i]
            if np.all(self.__board[i,0]==self.__board[i,:]) and self.__board[i,0] != 0: 

                return self.__board[i,0]
            
        #check diagonals
        if len(set([self.__board[i][i] for i in range(self.__size)]))==1 and self.__board[0,0]!=0: 

            return self.__board[0,0]
        if len(set([self.__board[i][self.__size-1-i] for i in range(self.__size)]))==1 and self.__board[0,-1]!=0: 

            return self.__board[0,-1]

        #check for full board
        if self.__move_num==self.__size**2: return 3

        return None
        
    def get_board(self):
        return self.__board

    def get_current_turn(self):
        return self.__current_turn

    def get_size(self):
        return self.__size
    