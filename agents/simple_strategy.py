from collections import Counter
import copy
import random
import numpy as np

class Simple_Strategy:
    def __init__(self,verbose=False):
        self.__verbose = verbose

    def __verbose_print(self,message):
        if self.__verbose:
            print(message)
            

    def make_move(self,game):
        "checks for advantagious moves in order of advantage and plays optimal move"
        board = game.get_board()
        self.__size = game.get_size()
        self.__ident = game.get_current_turn()
        one_aways = self.check_one_aways(board)

        #check if there is winning move and play it
        if len(one_aways[self.__ident]) >0:
            self.__verbose_print('made winning move')
            return one_aways[self.__ident][0]

        #check if opponent has winning move and block it
        if len(one_aways[((self.__ident-2)%2)+1])>0:
            self.__verbose_print('blocked winning move')
            return one_aways[((self.__ident-2)%2)+1][0]
        

        #check if any moves to create trap, i.e sets up 2 possible winning moves
        open = np.where(board==0)
        open_pos = list(zip(open[0],open[1]))
        single_winning = []

        for i in open_pos:
            sim_board = copy.deepcopy(board)
            #simulates possible move and finds outcomes
            sim_board[i[0],i[1]]=self.__ident
            if len(self.check_one_aways(sim_board)[self.__ident]) >=2:
                self.__verbose_print('set up 2 winning')
                return i
            if len(self.check_one_aways(sim_board)[self.__ident]) ==1:
                single_winning.append(i)
            
        
        #check if any moves to create single winning move
        if len(single_winning)>0:
            self.__verbose_print('created single winning')
            return single_winning[0]

        #return random valid move
        return random.choice(open_pos) 


    def check_one_aways(self,board):
        "search for lines one move away from a win"
        #dictionary holds locations of winning moves for both players
        instances = {1:[],2:[]}

        for i in range(self.__size):
            #search for horizontal and vertical winning moves
            horiz = dict(Counter((board[:,i])))
            vert = dict(Counter((board[i,:])))
            if 0 in horiz.keys():
                if len(horiz)==2 and horiz[0] == 1:
                    instances[max(horiz, key=horiz.get)].append((int(np.where(board[:,i]==0)[0]),i))
            
            if 0 in vert.keys():
                if len(vert)==2 and vert[0] == 1:
                    instances[max(vert, key=vert.get)].append((i,int(np.where(board[i,:]==0)[0])))
                    
                    
        #search for diagonal winning moves
        left = [board[i][i] for i in range(self.__size)]
        right = [board[i][self.__size-1-i] for i in range(self.__size)]
        left_dict = dict(Counter(left))
        right_dict = dict(Counter(right))

        if 0 in left_dict.keys():
            if len(left_dict)==2 and left_dict[0]==1:
                instances[max(left, key=left_dict.get)].append((left.index(0),left.index(0)))
        if 0 in right_dict.keys():
            if len(right_dict)==2 and right_dict[0]==1:
                instances[max(right, key=right_dict.get)].append((right.index(0),self.__size-1-right.index(0)))

        return instances