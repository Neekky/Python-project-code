# -*- coding: utf-8 -*-

import random

import tkinter

# 定义关于球的类
class RandomBall():
    # 自动初始化画布和屏幕尺寸
    def __init__(self, canvas, scrnwidth, scrnheight):

        self.canvas = canvas
        # 定义球的初始位置（x，y），此坐标为球的圆心，位置随机生成
        self.xpos = random.randint(10, int(scrnwidth) - 20)
        self.ypos = random.randint(10, int(scrnheight) - 20)
        # 定义球在x、y方向上的移动速度，速度随机给定
        self.xvelocity = random.randint(6, 12)
        self.yvelocity = random.randint(6, 12)
        # 将屏幕尺寸的形参赋给函数内部
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        # 定义球的半径，半径大小随机给定
        self.radius = random.randint(40, 70)
        #定义球的颜色
        c = lambda:random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())
    # 创建球的函数
    def creat_ball(self):
        # 通过圆心，获取一矩形左上角和右下角的坐标
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        # tkinter没有创建圆的函数，通过创建椭圆的方式来生成圆
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color,outline=self.color)

    # 创建球移动的函数
    def move_ball(self):
        # 球的（x，y）坐标根据速度变化不断更新
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        # 当球撞到屏幕边界后，反弹的算法判断
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity = -self.xvelocity

        if self.xpos - self.radius <= 0:
            self.xvelocity = -self.xvelocity

        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity

        if self.ypos - self.radius <= 0:
            self.yvelocity = -self.yvelocity
        # 在画布上移动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)

# 定义屏保的类
class ScreenSaver():

    def __init__(self):

        self.balls = []
        # 每次启动程序，球的数量随机
        self.num_balls = random.randint(6, 20)
        # 生成root主窗口
        self.root = tkinter.Tk()
        #获取屏幕尺寸，作为主窗口尺寸
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        # 取消边框
        self.root.overrideredirect(1)
        # 调整背景透明度
        self.root.attributes('-alpha', 1)
        # 点击鼠标、移动鼠标、敲击键盘时退出程序
        self.root.bind('<Motion>', self.myquit)
        self.root.bind('<Any-Button>',self.myquit)
        self.root.bind('<Key>', self.myquit)
        # 创建画布，包括画布的归属、尺寸和背景颜色
        self.canvas = tkinter.Canvas(self.root,width=self.width,height=self.height,bg = "black")
        self.canvas.pack()

        # 根据num_balls随机生成的数值，在画布上生成球
        for i in range(self.num_balls):
            # 调用RandomBall函数，自动初始化出不同大小、位置和颜色的球
            ball = RandomBall(self.canvas,scrnwidth=self.width, scrnheight=self.height)
            # 调用生成球的函数
            ball.creat_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()
    # 调动球运动的函数
    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        # after函数是每200毫秒后启动一个函数，第二个参数为需启动的函数，类似于递归
        self.canvas.after(50, self.run_screen_saver)
    # 定义一个停止运行的函数
    def myquit(self, event):
        self.root.destroy()
# 调用函数
if __name__ == '__main__':
    ScreenSaver()