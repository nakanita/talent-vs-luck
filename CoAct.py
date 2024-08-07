# -*- coding: utf-8 -*-
#
# 複数のActを束ねて取りまとめるクラス
# アプリケーション上では、”RootAct"という名前で全てのActの大元に位置付けられる。

from BaseAct import BaseAct

class CoAct(BaseAct):
    
    type = "Co"
    
    def __init__(self):
        super().__init__()
        
        self.ActBuffer = []
        self.ActDict = {}    # 名前付きActを登録しておく
        return
    
    def action(self):
        for a_act in self.ActBuffer:
            a_act.action()
        return
    
    def draw(self):
        for a_act in self.ActBuffer:
            a_act.draw()
        return
    
    def get_energy(self):
        eg = 0.0
        for a_act in self.ActBuffer:
            eg += a_act.get_energy()
        return eg
    
    # バッファ本体を得る
    def body(self):
        return self.ActBuffer
    
    # Actの追加
    def put(self, act, name=None):
        self.ActBuffer.append( act )
        if name is not None:    # 名前があれば辞書に追加する
            if name in self.ActDict: # 既に同じ名前があったらエラーとする
                raise NameError('Duplicate name, "' + name + '"')
            self.ActDict[name] = act
            act.name = name     # そのact本体にも名前を持たせる
    
    # 名前付きActを得る
    def get(self, name):
        if name in self.ActDict:
            return self.ActDict[name]
        else:
            return None # その名前が無かった

    # 名前付きActを削除する
    def remove(self, name):
        if name in self.ActDict:
            act = self.ActDict[name]
            self.ActBuffer.remove( act )
            del self.ActDict[name]

    # ActBuffer を出力してみる
    def printBody(self):
        print( "[" + ", ".join(map(str, self.ActBuffer)) + "]" ) # 文字列化->カンマ区切りで連結

    # ActDict を出力してみる
    def printDict(self):
        list = [ name + ":" +  str(self.ActDict[name]) for name in self.ActDict ]
        print( "{" + ", ".join(list) + "}" )

# テストコード
if __name__=="__main__":
    A = CoAct()
    
    A.put( "hello", "hello" )
    A.put( 3, "three" )
    A.put( "Tri", "Three" )
    A.put( 3.1415, "pi" )
    
    A.printBody()
    A.printDict()

