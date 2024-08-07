# talent-vs-luck
Simulation to see which is more important: talent or luck. Based on the paper for the Ignobel Prize 2022 in Economics.

Talent vs Luck のシミュレーションを試してみよう。

[TALENT VERSUS LUCK: THE ROLE OF RANDOMNESS IN SUCCESS AND FAILURE](https://www.worldscientific.com/doi/abs/10.1142/S0219525918500145)

### 環境設定：

画面描画に Pyglet を利用している。
    
    pip install pyglet

### 実行方法：

    python Main.py
    
* 設定値(グローバル変数)は G_Vals.py に記載されている。
* 実行終了すると、シミュレーション結果がjsonファイルに出力される。
        jsonファイル名 : TvL_YYYYMMDDhhmmss.json
        この jsonファイルは、ResultView.ipynb によって見ることができる。
