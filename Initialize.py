# -*- coding: utf-8 -*-
#
# 各Actの初期設定
# ここで実質的なアプリケーションの構成を行っている

from G_Vals import G_Vals
from CoAct import CoAct

from AgentAct import AgentAct
from BallAct import BallAct
from FixAct import FixAct
from CounterAct import CounterAct

# import numpy as np

class Initialize:

    def __init__(self):
        self.Globals = G_Vals.get_instance()
        self.RootAct = self.Globals.RootAct
        self.RootCollis = self.Globals.RootCollis

        # AgentAct は AgentCoAct の中にまとめておく
        self.AgentCoAct = CoAct()
        self.RootAct.put( self.AgentCoAct, "Agents" )
    
    def initRootAct(self):
        
        fix_act = self.initFix()

        a_list = []
        for i in range( G_Vals.N_AGENT ):
            a_act = self.initAgent(i)
            a_list.append( a_act )
        
        c_list = []
        for i in range( G_Vals.N_BALL ):
            c_act = self.initBall(i)
            c_list.append( c_act )
        
        self.initCouner()

        # 当たりバッファを構築する
        # Ball vs Fix
        for c_act in c_list:
            self.RootCollis.put( c_act, fix_act )
        
        # Ball vs Agent
        for c_act in c_list:
            for a_act in a_list:
                self.RootCollis.put( c_act, a_act )
    
    def initFix(self):
        act = FixAct()
        self.RootAct.put( act, "Fix" )
        return act

    def initAgent(self, id):
        act = AgentAct(id) # id番号を付与する
        # ここ、RootAct ではなく、AgentCoAct でまとめている
        self.AgentCoAct.put( act, "Agent_" + str(id) )
        return act
    
    def initBall(self, id):
        # 幸運フラグ -- 半分は幸運に、残り半分は不運に設定
        if id < G_Vals.N_BALL // 2 :
            good = True
        else:
            good = False
        
        act = BallAct(good)
        self.RootAct.put( act, "Ball_" + str(id) )
        return act
    
    def initCouner(self):
        act = CounterAct()
        self.RootAct.put( act, "Counter" )
        return act