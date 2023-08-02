from MyService import MyService
import tkinter
from tkinter.filedialog import askopenfilenames

class PlayWindow:
    def __init__(self, myserbise):
        self.myserbise = myserbise

    # 用户登录成功显示界面
    def showWindow(self):
        # 主窗口显示
        top = tkinter.Tk()
        top.title('音乐播放插件')
        # 组件插入
        self.createWidget(top)
        # 将音乐名插入到label01上
        self.insert_mname()
        top.mainloop()
    
    def createWidget(self,top):
        # 按扭设置
        btn01 = tkinter.Button(top, text='播放音乐')
        btn02 = tkinter.Button(top, text='导入音乐')
        btn03 = tkinter.Button(top, text='删除音乐')
        
        btn01.grid(row=0, column=0, padx=3)
        btn02.grid(row=0, column=3, padx=3)
        btn03.grid(row=0, column=6, padx=3)

        # 音乐列表
        self.label01 = tkinter.Listbox(top)
        self.label01.grid(row=1, column=0, columnspan=10)

        # 事件方法
        btn01.bind('<Button-1>', self.play_music)
        btn02.bind('<Button-1>', self.import_music)
        btn03.bind('<Button-1>', self.del_music)

    # 插入音乐名至列表
    def insert_mname(self):
        self.label01.delete(0,tkinter.END)
        music_name = self.myserbise.find_mname()
        for mname in music_name:
            self.label01.insert(tkinter.END, mname)
    
    def get_mname(self):
        # 获取音乐列表的选中的索引
        insert = self.label01.curselection()
        # 获取音乐名
        mname = self.label01.get(insert)
        return mname
        
    # 播放音乐
    def play_music(self,event):
        print('播放音乐')
        # 查询选中音乐名字
        mname = self.get_mname()
        # 查询音乐地址
        self.myserbise.play_music(mname)

    # 导入音乐
    def import_music(self,event):
        print('导入音乐')
        music_file = askopenfilenames(title='导入的音乐',
                                     initialdir='D:\music_file\cloud_music',
                                     filetypes=[("音乐文件",".mp3")])
        # 将音乐名及路径存入数据库
        self.myserbise.add_music(music_file)
        # 导入音乐后更新音乐列表
        self.insert_mname()

    # 删除音乐
    def del_music(self,event):
        try:
            print('删除音乐')
            # 查询选中音乐名字
            mname = self.get_mname()
            # 从关系表中删除用户与音乐行
            self.myserbise.del_list(mname)
            # 导入音乐后更新音乐列表
            self.insert_mname()
        except:
            print('没有选择项')

if __name__ == '__main__':
    uname = input('请输入用户名：')
    password = input('请输入密码：')
    myserbise = MyService()
    playwindow = PlayWindow(myserbise)
    # 判断用户是否存在
    if myserbise.login(uname,password):
        print('登录成功')
        # 进行用户界面
        playwindow.showWindow()
    else:
        print('登录失败')
