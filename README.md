# CalcAIC
モデル評価指標であるAIC(Akaike's Information Criterion)の計算をPythonで実装したものです．

利用する際にはまず参考サイトをご覧ください．


### テストデータによる検証
[CalcTestAIC.py](https://github.com/Atsuto0519/CalcAIC/blob/master/CalcTestAIC.py)
と
[plot_TestAIC.py](https://github.com/Atsuto0519/CalcAIC/blob/master/plot_TestAIC.py)
は[こちら](http://takashiyoshino.random-walk.org/memo/keikaku2/node5.html)に載っている
結果と同じになることを検証済み．


### [CalcAICtoLSM.py](https://github.com/Atsuto0519/CalcAIC/blob/master/CalcAICtoLSM.py)
指定したcsvファイルからデータを読み込み，指定した次数のLSMの近似線をプロットする．

また，指定した次数のLSMにAICを適用した結果も表示する．


### [plot_lsmAIC.py](https://github.com/Atsuto0519/CalcAIC/blob/master/plot_lsmAIC.py)
指定したcsvファイルからデータを読み込み，指定した次数までのLSMの近似線を全てプロットする．

また，指定した次数までのLSMにAICを適用した結果も表示する．


# 参考サイト
- [尤度とAIC](http://takashiyoshino.random-walk.org/memo/keikaku2/node5.html)
- [Python Tips：多重リストをフラットにしたい - Life with Python](http://www.lifewithpython.com/2014/01/python-flatten-nested-lists.html)


# インポートしたリポジトリ
- [LSM_regularization](https://github.com/Atsuto0519/LSM_regularization)
