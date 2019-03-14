class HouseItem():

    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '[%s]占地 %.2f'%(self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        #剩余面积
        self.free_area = area
        #家具列表
        self.item_list=[]
    def __str__(self):
        return ('房子户型是%s\n,总面积是%.2f[剩余面积是%s]\n家具%s'
                %(self.house_type,self.area,
                  self.free_area,self.item_list))
    def add_item(self,item):
        print('要添加的家具:%s'%item)
        #1.判断面积
        if item.area > self.free_area:
            print('%s 面面积太大，放不下' % item.name)
            return
        #2.添加家具列表
        self.item_list.append(item.name)
        #3.计算剩余面积
        self.free_area -=  item.area

bed=HouseItem('席梦思',3)
chest=HouseItem('衣柜',15)
table=HouseItem('桌子',30)

my_home=House('二室一厅',65)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)