# -*- coding: utf-8 -*-
#
# 幸運・不運イベントを表すAct。
# 画面上では赤、または青の丸として描かれる。

#import pyglet
from pyglet.gl import *

import numpy as np

from BaseAct import BaseAct
from G_Vals import G_Vals

class BallAct(BaseAct):
    
    Globals = G_Vals.get_instance()
    
    type = "Ball"
    
    velo = 2.0      # 移動速度
    radius = 2.0    # 半径
    
    def __init__(self, good:bool):
        super().__init__()
        
        self.RootAct = self.Globals.RootAct
        self.good = good    # 幸運フラグ、Falseなら不幸
        if good:
            self.color = (255, 0, 0) # 幸運は赤
        else:
            self.color = (0, 0, 255) # 不運は青
        
        self.init_pos()
    
    # ランダムな位置に初期化
    def init_pos(self):
        self.p = (self.Globals.FIELD_WIDTH, self.Globals.FIELD_HEIGHT ) \
                    * (np.random.rand(2) - 0.5)
    
    def action(self):
        # ランダムな角度に、一定速度 veloで移動する
        th = 2 * np.pi * np.random.rand()
        self.v[0] = self.velo * np.cos(th)
        self.v[1] = self.velo * np.sin(th)

        # 移動
        self.p += self.v
        return
    
    def draw(self):
        try:
            quad = gluNewQuadric()    # GLUオブジェクトのメモリ確保
            # gluQuadricNormals(quad, GLU_SMOOTH)
                # 二次曲面に設定する法線の種類を指定する
                # GLU_SMOOTH : 二次曲面の各頂点に対してひとつの法線を生成する(default)
            
            self.draw_sphere(quad, self.p[0], self.p[1], 0.0 )
            
        finally:
            gluDeleteQuadric(quad)
    
    def draw_sphere(self, quad, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glColor3ub(*self.color)
        gluSphere(quad, self.radius, 16, 16)
        glPopMatrix()
