# -*- coding: utf-8 -*-
#
# グローバル変数

from Singleton import Singleton
from CoAct import CoAct
from Collis import Collis

class G_Vals(Singleton):
    
    RootAct = CoAct()
    RootCollis = Collis()
    
    N_AGENT = 1000  # エージェントの数
    N_BALL = 500    # 幸運・不運イベントの数
    
    # 作業フィールドの大きさ -> FixAct の範囲に設定される
    FIELD_WIDTH = 200
    FIELD_HEIGHT = 200

    # 才能と財産の初期値 -> AgentAct に設定される
    TALENT_MEAN = 0.6
    TLENT_SDEV = 0.1
    INIT_CAPITAL = 10.0

    # シミュレーションの実行ターン
    TurnCount = 0
    MAX_TURN = 100
    COUNT_INTERVAL = 10 # カウントを行うターン間隔
