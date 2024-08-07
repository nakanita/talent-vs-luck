# -*- coding: utf-8 -*-
#

# import numpy as np

class HitFunc():
    
    # 環境との当たり（巡回移動）
    def hit_circle_env(self, act1, act2, args):
        # act2 には FixAct を期待している 
        sect = args[0]  
        if sect == 1:
            act1.p[0] -= (act2.RIGHT - act2.LEFT)
        elif sect == 2:
            act1.p[0] += (act2.RIGHT - act2.LEFT)
        
        if sect == 3:
            act1.p[1] -= (act2.TOP - act2.BOTTOM)
        elif sect == 4:
            act1.p[1] += (act2.TOP - act2.BOTTOM)
        
        return
    
    # BallとAgentとの当たり
    def hit_point_point(self, from_act, to_act, args):
        
        # print(f"HIT! {from_act.name} : {to_act.name}")
        if from_act.good:   # 幸運フラグ
            to_act.lucky()  # 幸運なイベント
        else:
            to_act.unlucky()    # 不運なイベント
        return