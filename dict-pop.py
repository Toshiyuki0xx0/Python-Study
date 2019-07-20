#今回集計するデータ
s = """
サンマ,カツオ,サンマ,サンマ,マグロ,ふぐ,マグロ,マグロ,ニシン
"""

#データの前後空白を除去
s = s.strip()
#カンマでデータを区切る
s_list = s.split(",")

#集計用の辞書を生成
result = {}  #空の辞書型変数を作成
for name in s_list:
    name = name.strip()
    if not name in result:
        result[name] = 0
    result[name] = result[name] + 1
for name,value in result.items():
    print(name + "=" + str(value))
    
