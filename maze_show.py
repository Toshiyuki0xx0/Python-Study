from tkinter import *

tile_size = 20 # 描画タイルのサイズ

#迷路データを取り込む
def load_map_data():
    from maze_data import data #maze_data.pyのdataを取り込む
    return data

#迷路を表示する関数
def draw_map(cv,data):
    #左上から右下へと描画
    rows = len(data) #迷路の行数
    cols = len(data[0]) #迷路の列数
    for y in range(rows):
        y1 = y * tile_size
        y2 = y1 + tile_size
        for x in range(cols):
            x1 = x * tile_size
            x2 = x1 + tile_size
            # xとyの値から、対応するdataリストの値を得る
            p = data[y][x]
            #値に応じた色を決定する
            if p == 0: color = "white"
            if p == 1: color = "#404040"  #灰色
            if p == 2: color = "red"
            if p == 3: color = "blue"
            #正方形を描画
            cv.create_rectangle(x1,y1,x2,y2,
                                fill=color,
                                outline="black",width=2) #枠線
#ウィンドウとキャンバスを作成
def create_window(map_data,events=[]):
    win = Tk()
    win.title("迷路")
    rows = len(map_data)
    cols = len(map_data[0])
    cv = Canvas(win,
                width=(cols * tile_size),
                height=(rows * tile_size))
    cv.pack()
    draw_map(cv,map_data)
    for func in events: func(cv,map_data)
    win.mainloop()

if __name__ == "__main__":
    map_data = load_map_data()
    create_window(map_data)
