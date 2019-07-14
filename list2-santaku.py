#3択クイズ
#クイズデータを2次元のリストで表現
quiz_list = [
    #[問題,選択肢1,選択肢2,選択肢3,答え]
    ["夏目漱石の本名は？","石男","浩介","金之助",3],
    ["野口英世が亡くなった場所は？","福島","ガーナ","パリ",2],
    ["福沢諭吉が広めたものは？","カレー","電灯","天ぷら",1],
    ["樋口一葉が書いた小説は？","双葉","十三夜","歌世界",2]
]

#問題をシャッフル
import random
random.shuffle(quiz_list)

for quiz in quiz_list:
    print("[問題]")
    print(quiz[0])
    for i in range(3):
        no = i + 1
        print(str(no) + ":" + quiz[no])
    user = int(input("答えは？"))
    ans = quiz[4]
    if user == ans:
        print("正解")
    else:
        print("はずれ")
    print("---")
