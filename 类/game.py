class Game(object):
        top_score = 0
        def __init__(self,player):
            self.player=player
        @staticmethod
        def show_help():
            print('帮助信息')
        @classmethod
        def show_top_score(cls):
            print('最高分:%s'%Game.top_score)
        def start_game(self):
            print('%s 开始游戏'%self.player)

Game.show_top_score()
Game.show_help()
xiaoming = Game('xiaoming')
xiaoming.start_game()