import copy
from tqdm import tqdm
class Complete_Tree_Search:
    def __init_(self):
        pass


    def check_state(self,board,size,move_num,agent_ident):
                    
        #check vertical and horiz lines
        for i in range(size):
            if np.all(board[0,i]==board[:,i]) and board[0,i] != 0:
                if board[0,i] == agent_ident:
                    return 1
                else:
                    return -100
            if np.all(board[i,0]==board[i,:]) and board[i,0] != 0:
                if board[i,0] == agent_ident:
                    return 1
                else:
                    return -100
            
        #check diagonals
        if len(set([board[i][i] for i in range(size)]))==1 and board[0,0]!=0: 
            if board[0,0] == agent_ident:
                return 1
            else:
                return -100
        if len(set([board[i][size-1-i] for i in range(size)]))==1 and board[0,-1]!=0:
            if board[0,-1] == agent_ident:
                return 1
            else:
                return -100

        #check for full board
        if move_num==size**2: return 0

        return None

    def make_move(self,game):
        
        open = np.where(game.get_board()==0)
        open_pos = list(zip(open[0],open[1]))

        max_val = -float('inf')
        best_move = []
        for i in open_pos:#tqdm(open_pos):
            move_val = self.recurse(game.get_board(),i,game.get_current_turn(), game.get_current_turn(),game.get_num_move())
            #print("move val : {}".format(move_val))
            if move_val > max_val:
                max_val = move_val
                best_move=i

      

        return best_move

    def recurse(self,board,move,current_turn,agent_ident,move_num):
        #add move to board
        board_copy = copy.deepcopy(board)
        board_copy[move[0],move[1]]=current_turn
        
        #checks if game is finished
        current_state = self.check_state(board_copy,len(board[0]),move_num+1,agent_ident)
        if current_state != None:
            return current_state

        #finds open positions on board
        open = np.where(board_copy==0)
        open_pos = list(zip(open[0],open[1]))

       
        #if agent is playing
        if current_turn == agent_ident:
            ave_value = 0
            for i in open_pos:
                ave_value+=self.recurse(board_copy,i,((current_turn-2)%2)+1,agent_ident,move_num+1)
            return ave_value/len(open_pos)

        #if opponent is playing
        else:
            max_val =-float('inf')
            for i in open_pos:
                move_val = self.recurse(board_copy,i,((current_turn-2)%2)+1,agent_ident,move_num+1)
                if move_val > max_val:
                    max_val = move_val
            return max_val