class MusicPlay(object):
    #记录第一个被创建对象引用
    instance=None
    #记录是否执行过初始化
    flag=False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance
    def __init__(self):
        #判断是否执行过初始化动作
        if MusicPlay.flag:
            return
        #如果没执行执行初始化动作
        print('初始化播放器')

        #修改类属性的标记
        MusicPlay.flag=True


play1=MusicPlay()
print(play1)

play2=MusicPlay()
print(play2)