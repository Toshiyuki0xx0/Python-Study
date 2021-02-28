value = 30 #グローバル変数の定義
def hoge1():
    print(value) #グローバル変数を参照
def hoge2():
    value = 999
    print(value) #グローバル変数を参照
hoge1()
hoge2()
print(value)
