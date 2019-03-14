class Woman:
    def __init__(self,name):
        self.name=name
        self.__age=18
    def __secret(self):
        print('%s 的年龄是%s'%(self.name,self.__age))
xiaofang = Woman('xiaofang')
#print(xiaofang.__age)
xiaofang.__secret()