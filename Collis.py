# -*- coding: utf-8 -*-
#

import ColFunc
import HitFunc

class Collis():
    
    def __init__(self):
        self.ColBuffer = []
        self.colfunc = ColFunc.ColFunc()
        self.hitfunc = HitFunc.HitFunc()
        
        # 当たり判定関数テーブルをセット
        self.colfunc_tbl = {
            "Ball":{
                    "Fix" : self.colfunc.check_circle_env,
                    "Agent": self.colfunc.check_point_point,
                }
        }
        
        # 当たり処理関数テーブルをセット
        self.hitfunc_tbl = {
            "Ball":{
                    "Fix" : self.hitfunc.hit_circle_env,
                    "Agent": self.hitfunc.hit_point_point,
            }
        }
    
    # バッファを空にする
    def clear(self):
        self.ColBuffer.clear()
        return
    
    # 当たり対象Actの追加
    def put(self, act1, act2):
        self.ColBuffer.append( (act1, act2) )
    
    # 当たり判定実行
    def run(self):
        for (act1, act2) in self.ColBuffer:
            # 当たり判定
            is_hit, args = (self.colfunc_tbl[act1.type][act2.type])( act1, act2 )
            
            if is_hit:
                # 当たったときの処理
                (self.hitfunc_tbl[act1.type][act2.type])( act1, act2, args )
            
