class Tool(object):
    count = 0
    @classmethod
    def show_tools_count(cls):
        print('%s'%cls.count)

    def __init__(self,name):
        self.name=name
        Tool.count+=1

tool1=Tool('斧头')
tool2=Tool('大刀')

Tool.show_tools_count()