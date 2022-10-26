# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。

import math
def print_sum(a, b):
    c = math.sin(a + b)
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    print(f'{a}と{b}を足してsin({a+b})をとると{c}になるらしい。')  # Ctrl+F8を押すとブレークポイントを切り替えます。

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__': # なくてもよい
    x = int(input("xの値? "))
    y = int(input("yの値? "))
    print_sum(x, y)

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
