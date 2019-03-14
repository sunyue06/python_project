class Gun:
    def __init__(self,model):
        self.model=model
        self.bullet_count=0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        #1.判断子弹数量
        if self.bullet_count <=0:
            print('子弹不足，无法射击')
            return
        #2.发射子弹 -1
        self.bullet_count -=1
        #3.反馈信息
        print('命中,当前子弹数%s' %self.bullet_count)

class Soldier:
    def __init__(self,name):
        self.name=name
        self.gun=None

    def fire(self):
        #1.判断是否有枪
        if self.gun==None:
            print('%s 没有枪'%self.name)
            return
        self.gun.add_bullet(50)
        self.gun.shoot()
#1.创建枪
ak47=Gun('AK47')
#2.创建士兵
xusanduo = Soldier('许三多')
#xusanduo.gun=ak47
xusanduo.fire()
print(xusanduo.gun)
