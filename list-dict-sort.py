#あるクラスのテスト結果
test_list = [
    {"名前":"田中","国語":80,"算数":45,"社会":90},
    {"名前":"鈴川","国語":70,"算数":60,"社会":80},
    {"名前":"早川","国語":90,"算数":30,"社会":100}
    ]
#国語の合計点を求める
total = 0
for p in test_list:
    p["合計"]  = p["国語"] + p["算数"] + p["社会"]
    print(p)
test_list = sorted(test_list,key=lambda v: v["社会"],
                   reverse=True)
for p in test_list:
    print(p)

    
