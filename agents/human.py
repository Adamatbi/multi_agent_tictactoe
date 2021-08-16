class Human:
    def __init__(self):
        pass

    def make_move(self,game):
        game.display()
        size = game.get_size()
        while True:
            print('player {} choose your position with space between number:'.format(game.get_current_turn()))
            move = input()
            try:
                x,y = move.split(' ')
                y = int(y)
                x = int(x)
                return (size-1-y,x)
            except:
                print('invalid input')