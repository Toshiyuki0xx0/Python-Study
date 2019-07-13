#あるクラスの国語の点数  ---  (*1)
points = [62,58,72,60,47,81,74,65,59,38]

#各点数の平均を求める   ---  (*2)
total = 0;
for pt in points: #繰り返すたびにpointsの要素を一つずつptに代入
    total = total + pt #totalにptの値を足す
print("合計点=" + str(total))

#平均点を求める ---    (*3)
ave = total / len(points)  #合計を、pointsの要素数で割る
print("平均点="  +  str(ave))
