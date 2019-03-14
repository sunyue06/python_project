from tkinter import * #导入库
import requests
from bs4 import BeautifulSoup
#爬取网易云音乐
#获取页面的源代码
# 爬取网页数据
def download_song():
    #每次开始重新下载的时候删除listBox里面的所有的内容
    text.delete(0,END)
    # 获取用户输入的URL地址
    url = entry.get()
    # url = "https://music.163.com/playlist?id=2302000737"

    #下载地址
    song_url = "http://music.163.com/song/media/outer/url?id={}"
   #request请求类库，直接获取的html源代码
    result = requests.get(url,headers=header)
    # 对获取的html源代码进行处理，beautifulSoup对源码的处理
    html = BeautifulSoup(result.text,'html.parser')
    print(html)
    # 过滤元素，查找ul标签，class为f-hide，再去查找里面的所有a标签，返回的是一个数组
    musics = html.find('ul',{'class','f-hide'}).find_all('a')
    print(musics)
    music_dict = {}
    # 每个榜单数量太大，这里只下载5首歌曲
    for music in musics[:5]:
        #获取a标签对应的href，并过滤掉前面的song?id=，只留下歌曲的id
        music_id = music.get('href').strip('/song?id=')
        #获取歌曲的名称
        music_name = music.text
        #组装为一个字典
        music_dict[music_id] = music_name
   
    # 遍历字典，下载每首歌曲，并保存到本地
    for k, v in music_dict.items():
        download_url = song_url.format(k)
        saveMusic(download_url,v)
def saveMusic(download_url,music_name):
    # 拿到下载路径和文件保存路径
    #在listbox中输出正在下载的文件和状态
    text.insert(END,'正在下载>>>>:' + music_name)
    # 拼接下载路径地址
    file_path = '/Users/'+getpass.getuser()+'/Downloads/musics'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    # 保存的文件名
    save_path = file_path + '/%s.mp3' % music_name
    print(save_path)

    # 开始下载数据
    result = requests.get(download_url, headers=header)
    with open(save_path, 'wb') as w_obj:
        w_obj.write(result.content)
    text.insert(END,'下载完成:>>>>' + music_name)
    # 跳转到指定的item索引位置
    text.see(text.size()-1)



#搭建界面

#创建窗口
root = Tk()

#窗口标题
root.title("网易云音乐")

#窗口大小    小写的x          
root.geometry("550x400+560+260")

#窗口的位置
#root.geometry("+550+230")
#标签控件
label = Label(root,text="请输入要下载的歌单URL:",font = ('华文行楷',10))

#定位
label.grid()

#输入框
entry = Entry(root,font = ('微软雅黑',25))

#定位
entry.grid(row = 0,column = 1)

#列表控件
text = Listbox(root,font = ('微软雅黑',15),width = 45,height = 10)

#组件所跨越的列数
text.grid(row = 1,columnspan = 2)

#点击按钮
button = Button(root,text = "开始下载",font = ('微软雅黑',15),command = downlaod_song())
#对齐
button.grid(row = 2,column = 0,sticky = W)
#点击触发的方法
button1 = Button(root,text = "退出",font = ('微软雅黑',15),command = root.quit)
button1.grid(row = 2,column = 1,sticky = E)

#显示窗口
root.mainloop()


#爬取网易云音乐
