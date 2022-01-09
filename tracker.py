import matplotlib.pyplot as plt
from time import sleep
from Tkinter import *
import thread

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)

def getxy():
    with open('rosbag.csv') as f:
        lines = f.readlines()
    [x,y] = lines[0].split(',')
    return ((float(x))//0.1+200,(float(y))//0.1+100)
       
def update(x,y):
    while(1):
        (x1,y1) = getxy()
        ###print(x1,y1)
        canvas.move('square',-x+x1,-y+y1)
        (x,y) = (x1,y1)

def main():
    (x,y) = getxy()
    canvas.delete("all")
    img = PhotoImage(file="levine.pgm")      
    canvas.create_image(20,20, anchor=NW, image=img)
    canvas.create_rectangle(x,y,x+10,y+10,fill=('red'),tags=('square'))
    canvas.create_rectangle(38,75,313,220)
    canvas.create_rectangle(93,115,273,180)
    canvas.pack()
    thread.start_new_thread(update,(x,y))
    root.mainloop()


if __name__ == "__main__":
    main()


