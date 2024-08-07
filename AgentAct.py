# -*- coding: utf-8 -*-
#

#import pyglet
from pyglet.gl import *

import numpy as np

from BaseAct import BaseAct
from G_Vals import G_Vals

class AgentAct(BaseAct):
    
    Globals = G_Vals.get_instance()
    
    type = "Agent"
    
    # 才能と財産の初期値
    TALENT_MEAN = Globals.TALENT_MEAN
    TLENT_SDEV  = Globals.TLENT_SDEV
    INIT_CAPITAL = Globals.INIT_CAPITAL
    
    radius = 1.0;   # 半径
    
    def __init__(self, id):
        super().__init__()
        
        self.RootAct = self.Globals.RootAct
        self.id = id    # id番号を付けておこう

        self.init_pos()
        self.init_values()
    
    # ランダムな位置に初期化
    def init_pos(self):
        self.p = (self.Globals.FIELD_WIDTH, self.Globals.FIELD_HEIGHT ) \
                    * (np.random.rand(2) - 0.5)
    
    def init_values(self):
        # 持てる才能は正規分布から[0,1]の範囲を切り出す
        self.talent = -1.0
        while (self.talent < 0.0 or 1.0 < self.talent):
            self.talent = np.random.normal( loc=self.TALENT_MEAN, scale=self.TLENT_SDEV )
        
        # 持てる財産は同じ初期値を与える
        self.capital = self.INIT_CAPITAL

        # 幸運、不運のカウント
        self.n_lucky = 0
        self.n_unlucky = 0
    
    # 幸運なイベント
    def lucky(self):
        # 能力に応じて財産が増える
        self.capital *= (1 + self.talent) 
        self.n_lucky += 1
        
    # 不幸なイベント
    def unlucky(self):
        # 財産を半分にする
        self.capital *= 0.5
        self.n_unlucky += 1
    
    # def action(self):
    #   # 何もしない、動かない
    #   return
    
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
        
        glColor4f(0.0, 1.0, 0.0, 0.7) # 点の色、半透明にしよう

        gluSphere(quad, self.radius, 16, 16)
        glPopMatrix()
    