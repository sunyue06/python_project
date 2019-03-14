import random
class Game:#定义一个游戏类
    def __init__(self,i,player1,player2):
        self.player1=player1
        self.player2=player2
        print('初始化已成功，开始游戏')
    def start_game(self):
        self.player1.cast()
        self.player2.cast()
        #player1_dice_count_list = [self.player1.dices[0], self.player1.dices[1], self.player1.dices[2]]
        #player2_dice_count_list = [self.player2.dices[0], self.player2.dices[1], self.player2.dices[2]]
        #print('玩家1抛筛子之后的点数为%s'%str(player1_dice_count_list))
        #print('玩家1抛筛子之后的点数为%s' % str(player2_dice_count_list))
        print(self.player1)
        print(self.player2)
class Player:#定义玩家类
    def __init__(self,name,sex,*dice):
        self.name=name
        self.sex=sex
        self.dices=dice  #表示该玩家拥有的骰子列表（元组）
    def cast(self):#玩家投掷骰子
        for dice in self.dices:
            dice.move()
    def guess_dice(self):
        return(4,2)
    def __str__(self):
        play_dice_count_list=[self.dices[0].count,self.dices[1].count,self.dices[2].count]
        return '玩家%s抛出的点数为%s'%(self.name,play_dice_count_list)
class Dice:#定义骰子类
    def __init__(self):
        self.count=0
    #筛子滚动的方法，滚动之后该骰子点数
    def move(self):
        self.count=random.randint(1,6)  #random.randint随机方法
#定义六个骰子
d1=Dice()
d2=Dice()
d3=Dice()
d4=Dice()
d5=Dice()
d6=Dice()
#传入玩家
p1=Player('王昕','男',d1,d2,d3)
p2=Player('林巧云','女',d4,d5,d6)
#控制玩的次数
for i in range(1,11):
    print('------第%s次游戏情况------' % i)
    game=Game(10,p1,p2)
    game.start_game()




