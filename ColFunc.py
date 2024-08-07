# -*- coding: utf-8 -*-
#

import numpy as np

class ColFunc():
    
    CHECK_DIST = 1.0   # BallとAgentが当たりと判定される距離
    
    # def __init__(self):
    #   return

    # 円と固定環境（外壁）との衝突判定
    # @classmethod
    def check_circle_env(self, act1, act2):
        # act2 には FixAct を期待している
        if act1.p[0] > act2.RIGHT:
            return ( True, [1] )
        elif act1.p[0] < act2.LEFT:
            return ( True, [2] )
        
        if act1.p[1] > act2.TOP:
            return ( True, [3] )
        elif act1.p[1] < act2.BOTTOM:
            return ( True, [4] )
        
        return ( False, [0] )
    
    # 点と点の当たり判定、一定の距離以内が基準
    @classmethod
    def check_point_point(self, act1, act2):

        # 先にXY範囲でチェックして高速化を図る
        if np.abs(act2.p[0] - act1.p[0]) > self.CHECK_DIST:
            return ( False, [] )
        if np.abs(act2.p[1] - act1.p[1]) > self.CHECK_DIST:
            return ( False, [] )
        
        # 本チェック
        dist = np.linalg.norm( (act2.p[0] - act1.p[0], act2.p[1] - act1.p[1]) )
        if dist <= self.CHECK_DIST:
            return ( True, [] )
        return ( False, [] )