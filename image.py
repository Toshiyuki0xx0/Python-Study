from tkinter import *
from PIL import ImageTk, Image

win = Tk()
cv  = Canvas(win,width=600,height=450)
cv.pack()

filename = "photo.jpg"
img = Image.open(filename)
print("size={0}x{1}".format(img.width,img.height))

img_tk = ImageTk.PhotoImage(img)

cv.create_image(0,0,image=img_tk, anchor=NW)

win.mainloop()
