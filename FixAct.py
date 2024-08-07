# -*- coding: utf-8 -*-
#

#import pyglet
from pyglet.gl import *

import numpy as np

from BaseAct import BaseAct
from G_Vals import G_Vals

class FixAct(BaseAct):
    
    Globals = G_Vals.get_instance()
    
    type = "Fix"

    def __init__(self):
        self.RIGHT   =  self.Globals.FIELD_WIDTH // 2
        self.LEFT    =  - self.Globals.FIELD_WIDTH // 2
        self.TOP     =  self.Globals.FIELD_HEIGHT // 2
        self.BOTTOM  =  - self.Globals.FIELD_HEIGHT // 2
        return
    
    # def action(self):
    #   # 何もしない、動かない
    #   return
    
    def draw(self):
        # glPushMatrix()
        # glTranslatef( self.p[0], self.p[1], 0 )
        
        glLineWidth( 10.0 )
        glBegin(GL_LINE_LOOP);  # 閉じたループならこっちの方が速い
        glColor3f(0.8, 1.0, 1.0)
        glVertex3f( self.RIGHT, self.TOP, 0 )
        glVertex3f( self.LEFT, self.TOP, 0 )
        glVertex3f( self.LEFT, self.BOTTOM, 0 )
        glVertex3f( self.RIGHT, self.BOTTOM, 0 )
        glEnd()
        
        # glPopMatrix()
