# -*- coding: utf-8 -*-
#
# イグノーベル賞2022経済学賞の論文 : 才能か運か？ 
# Talent vs Luck のシミュレーションを試してみよう。
# 
# TALENT VERSUS LUCK: THE ROLE OF RANDOMNESS IN SUCCESS AND FAILURE
# https://www.worldscientific.com/doi/abs/10.1142/S0219525918500145
# 
# 画面描画に Pyglet を利用した。

import pyglet
# Disable error checking for increased performance
# pyglet.options['debug_gl'] = False
from pyglet.gl import *

from G_Vals import G_Vals
from Initialize import Initialize

# イベントを拾うため Window の SubClass とした
class Main( pyglet.window.Window ):
    
    def __init__(self):
        try:
            # Try and create a window with multisampling (antialiasing)
            config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True)
            super().__init__( resizable=True, config=config )
        except pyglet.window.NoSuchConfigException:
            # Fall back to no multisampling for old hardware
            super().__init__( resizable=True )
        
        self.Globals = G_Vals.get_instance()
        self.RootAct = self.Globals.RootAct
        self.RootCollis = self.Globals.RootCollis
    
    def initGL(self):
        glClearColor( 0/255, 20/255, 30/255, 1 ) # 背景色の設定
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_POINT_SMOOTH)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_COLOR_MATERIAL) # 1
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        # Define a simple function to create ctypes arrays of floats:
        def vector(*args):
            return (GLfloat * len(args))(*args)
        
        glLightfv(GL_LIGHT0, GL_POSITION, vector(0.5, 0.5, 3, 1))
        glLightfv(GL_LIGHT0, GL_SPECULAR, vector(0.5, 0.5, -1, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, vector(1, 1, 1, 1))
        
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vector(1, 1, 1, 1))
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE) # 2
        # 1 & 2 mean that we can use glColor*() to color materials
    
    # 座標軸を描いてみよう
    def _draw_axes(self):
        glBegin(GL_LINES)                 # x-axis (traditional-style)
        glColor3f(1, 0, 0)
        glVertex3f( -1000, 0, 0)
        glVertex3f( 1000, 0, 0)
        glEnd()
        
        glBegin(GL_LINES)                 # y-axis (traditional-style)
        glColor3f(0, 1, 0)
        glVertex3f(0, -1000, 0)
        glVertex3f(0,  1000, 0)
        glEnd()
        
        # 正面から見た場合には不要
        # glBegin(GL_LINES)                 # z-axis (traditional-style)
        # glColor3f(0, 0, 1)
        # glVertex3f(0, 0, -1000)
        # glVertex3f(0, 0,  1000)
        # glEnd()
    
    def initActs(self):
        init = Initialize()
        init.initRootAct()
        
        # 座標軸の回転角度 -- 正面に固定しよう
        # self.xAngle =  0
        # self.yAngle =  0
    
        self.Globals.TurnCount = 0
    
    def run(self):
        self.initActs()
        self.initGL()
        
        pyglet.clock.schedule( self.update )
        pyglet.app.run()
    
    def update(self, dt):
        self.Globals.TurnCount += 1
        if self.Globals.TurnCount > self.Globals.MAX_TURN:
            self.close()
            self.finishActs()
            return  # ここで終了！
        
        # 進行ターン数を出力しておこう
        print( f"Do Turn {self.Globals.TurnCount}", flush=True)
        
        self.RootAct.action()
        self.RootCollis.run()

    # 終了時の処理
    def finishActs(self):
        # カウントしたデータを出力する
        count_act = self.RootAct.get("Counter")
        if count_act is not None:
            count_act.finish_action()
        else:
            print("WARNING: CounterAct is None.")
        return
    
    # @window.event
    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        
        glPushMatrix()
        glTranslatef(0, 0, -200)    # Z軸方向に少し離れてみる
        # 回転はしなくてよい
        # glRotatef(self.xAngle, 1, 0, 0)
        # glRotatef(self.yAngle, 0, 1, 0)
        self._draw_axes()

        self.RootAct.draw()
        
        glPopMatrix()
    
    # @window.event
    def on_resize(self, width, height):
        # Override the default on_resize handler to create a 3D projection
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60., width / float(height), .1, 1000.)
            # y方向のビュー角度 (度単位), アスペクト比, 
            # zNear:一番近いZ範囲を指定(常に正), zFar:一番遠いZ範囲を指定(常に正)
        glMatrixMode(GL_MODELVIEW)
        return pyglet.event.EVENT_HANDLED
    
    # @window.event
    def on_key_press(self, key, modifiers):        
        # ESC または Q_key で終了
        if key == pyglet.window.key.ESCAPE or key == pyglet.window.key.Q:
            print("Bye!")
            self.close()

if __name__=="__main__":
    me = Main()
    me.run()
