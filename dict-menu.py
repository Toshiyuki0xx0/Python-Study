#レストランのメニュー
menu_dict = {
    "洋風カレー":900,
    "オムライス":870,
    "ラザニア":790,
    "ハンバーグ定食":920,
    "トマトパスタ":720}

#全ての料理の値段を1.3倍する
import math
for key,value in menu_dict.items():
    value2 = math.ceil(value * 1.3)
    print(key + ":" +str(value) + "⇒" + str(value2) + "円")
    
