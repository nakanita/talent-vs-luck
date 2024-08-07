# -*- coding: utf-8 -*-
#

import numpy as np

class BaseAct:

    type = "Base"
    
    def __init__(self):
        self.p = np.zeros( 2 )   # 位置: x, y
        self.v = np.zeros( 2 )   # 速度: vx, vy
        self.mass = 1.0
        self.name = None
        return
    
    def action(self):
        return
    
    def draw(self):
        return