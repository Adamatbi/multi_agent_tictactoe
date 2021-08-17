from tqdm import tqdm
from tictactoe import *

class Arena:
    def __init__(self,agent_1,agent_2,size=3):
        self.__agent_1 = agent_1
        self.__agent_2 = agent_2
        self.__size = size

    def battle(self,iters=1):
        "plays 2 agents against each other for iter times and records results"
        wins_agent_1=0
        wins_agent_2=0
        ties=0
        #play iters number of games
        for i in tqdm(range(iters)):
            result = self.play()
            if result==1: wins_agent_1 +=1
            if result==2: wins_agent_2 +=1
            if result==3: ties +=1
        return (wins_agent_1,wins_agent_2,ties)

    def play(self):
        "plays game between 2 agents"
        turn1 = True
        game = TicTacToe(size = self.__size)
        result = None
        while True:
            if turn1: result = game.move(1,self.__agent_1.make_move(game))
            else: result = game.move(2,self.__agent_2.make_move(game))
            turn1 = not turn1
            if result is not None:
                return result

