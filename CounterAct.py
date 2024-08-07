# -*- coding: utf-8 -*-
#
# シミュレーション経過をメモリ上に記録し、終了時にファイル出力する。
# このカウンターは１つの（非表示）Act として構成されている。

# import numpy as np
# import pandas as pd

from BaseAct import BaseAct
from G_Vals import G_Vals

import json
import datetime

class CounterAct(BaseAct):
    
    Globals = G_Vals.get_instance()
    
    type = "Counter"

    def __init__(self):
        self.Globals = G_Vals.get_instance()
        self.RootAct = self.Globals.RootAct

        self.turns = [] # ターン数を記録する
        self.capitals = []  # 財産を記録する
        self.lucks = [] # 幸運カウントを記録する
        self.unlucks = [] # 不運カウントを記録する
        
        # この時点で Agents ができあがっている前提
        #  < Agents は Counterより先に用意すること
        self.AgentCoAct = self.RootAct.get("Agents")
        if self.AgentCoAct is None:
            print("WARNING: from Couner, AgentCoAct is None.")
        
        # カウントを行う間隔、グローバル変数に設定してある
        self.COUNT_INTERVAL = self.Globals.COUNT_INTERVAL
        return
    
    def action(self):
        if self.Globals.TurnCount % self.COUNT_INTERVAL == 0:
            # 一定間隔でカウントを行う
            self.turns.append( self.Globals.TurnCount ) # ターン数を記録する
            self.count()
        return
    
    def count(self):
        c_data = [] # 財産値
        l_data = [] # 幸運カウント
        u_data = [] # 不運カウント
        for a_act in self.AgentCoAct.body():
            c_data.append( a_act.capital )
            l_data.append( a_act.n_lucky )
            u_data.append( a_act.n_unlucky )
        
        # 記録をためる    
        self.capitals.append( c_data )
        self.lucks.append( l_data )
        self.unlucks.append( u_data )

    def finish_action(self):
        self.saveJson()
    
    def saveJson(self):
        now = datetime.datetime.now()
        dstr = now.strftime('%Y%m%d%H%M%S')

        # JSON作成、先頭に日付を入れておこう
        json_data = '{{"date": {}}}'.format(dstr)
        json_obj = json.loads(json_data)

        # 才能値を得る
        talents = self.get_talent()
        # print( talents )
        json_obj["Talents"] = talents

        for idx, c_data in enumerate(self.capitals):
            l_data = self.lucks[idx]
            u_data = self.unlucks[idx]

            sub_json_obj = {}
            sub_json_obj["Capital"] = c_data
            sub_json_obj["Lucky"] = l_data
            sub_json_obj["Unlucky"] = u_data
            # print( json.dumps(sub_json_obj, indent=4) )

            # ターン数を得る -> キー文字列に直す         
            turn = self.turns.pop(0)    # 先頭から１個ずつ取り出す
            turn_str = "TURN_{}".format(turn)

            json_obj[ turn_str ] = sub_json_obj
        
        # print( json.dumps(json_obj, indent=4) )
        
        # ファイルに保存する
        outfname = "TvL_{}.json".format(dstr)
        with open(outfname, 'w') as f:
            json.dump(json_obj, f, indent=4)
        return
    
    def get_talent(self):
        t_data = []
        for a_act in self.AgentCoAct.body():
            t_data.append( a_act.talent )
        return t_data
    
    # def draw(self):
    #     # 何もしない、表示しない
    #     return