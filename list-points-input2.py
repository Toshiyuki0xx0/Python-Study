#点数を初期化
points = []  #値をなにもいれていないリストの変数を用意
#繰り返し点数を入れる
while True:
    s = input("点数は？")
    if (s == "") or (s == "q"):break
    v = int(s)
    points.append(v)
total = 0
for v in points:
    total = total + v
print("合計点=" + str(total))
ave = total / len(points)
print("平均点=" + str(ave))
