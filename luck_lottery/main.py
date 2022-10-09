#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image, ImageTk
import tkinter
import threading
import time

widget = []
root = tkinter.Tk()
root.title('抽奖︿(￣︶￣)︿')
root.minsize(290, 370)
# 是否开启循环的标志
is_loop = False
# 是否运行的标志
is_run = False


class LuckLottery:
    def __init__(self):
        self.init_ui()

    def init_ui(self):
        global widget
        canvas_root = tkinter.Canvas(root, width=290, height=370)
        im_root = get_image('icon.jpg',290,370)
        canvas_root.create_image(290,370,image=im_root)
        canvas_root.pack()
        # 摆放按钮
        btn1 = tkinter.Button(root, text='Airpods', bg='green')
        btn1.place(x=20, y=20, width=70, height=70)
        btn2 = tkinter.Button(root, text='再来一次', bg='white')
        btn2.place(x=110, y=20, width=70, height=70)
        btn3 = tkinter.Button(root, text='乳胶抱枕', bg='white')
        btn3.place(x=200, y=20, width=70, height=70)
        btn4 = tkinter.Button(root, text='谢谢', bg='white')
        btn4.place(x=20, y=110, width=70, height=70)
        btn5 = tkinter.Button(root, text='膳魔保温杯', bg='white')
        btn5.place(x=200, y=110, width=70, height=70)
        btn6 = tkinter.Button(root, text='无线充电宝', bg='white')
        btn6.place(x=20, y=200, width=70, height=70)
        btn7 = tkinter.Button(root, text='iphone14', bg='white')
        btn7.place(x=110, y=200, width=70, height=70)
        btn8 = tkinter.Button(root, text='谢谢', bg='white')
        btn8.place(x=200, y=200, width=70, height=70)
        # 将所有选项组成列表
        widget = [btn1, btn2, btn3, btn5, btn8, btn7, btn6, btn4]
        # 开始按钮
        btn_start = tkinter.Button(root, text='开始', command=newtask, bg='green')
        btn_start.place(x=80, y=300, width=50, height=50)
        # 结束按钮
        btn_stop = tkinter.Button(root, text='结束', command=stop, bg='red')
        btn_stop.place(x=150, y=300, width=50, height=50)


def round():
    # 判断是否开始循环（防止多次按下开始按钮程序开启多次转盘循环）
    if is_loop == True:
        return
    # 初始化计数变量
    i = 0
    while True:
        # 延时操作
        time.sleep(0.001)
        # 将所有组件的背景颜色变为白色
        for j in widget:
            j['bg'] = 'white'
        # 将当前数值对应的组件变色
        widget[i]['bg'] = 'green'

        i += 1
        # 如果i大于最大索引直接归零
        if i >= len(widget):
            i = 0
        if is_run == True:
            continue
        else:
            break


# 开始事件
def newtask():
    global is_loop
    global is_run
    # 建立线程
    t = threading.Thread(target=round)
    # 开启线程运行
    t.start()
    # 设置循环开始标志
    is_loop = True
    # 是否运行的标志
    is_run = True


# 停止事件
def stop():
    global is_loop
    global is_run
    is_run = False
    is_loop = False


def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


if __name__ == '__main__':
    luck_lottery = LuckLottery()

    root.mainloop()
