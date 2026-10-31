from tkinter import *
from tkinter import messagebox as mb

i_wl = 0
pen_color = "black"

def draw(event):
    global i_wl
    x,y = event.x,event.y
    canvas.create_oval(x,y,x+i_wl,y+i_wl,fill=pen_color, outline=pen_color)

def wl():
    global i_wl
    s_wl = wl_entry.get().strip()
    try:
        i_wl = float(s_wl)
    except Exception as e:
        mb.showerror("Ошибка",f"Ошибка: {e}")

def wl_entry_bind(event):
    wl()



# def change_to_red(event):
#     global pen_color
#     pen_color = "red"


window = Tk()
window.title("Графический редактор")

canvas = Canvas(window,width=600,height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

# red_label = Label(bg="red", width=8,height=2)
# red_label.pack(side=LEFT)
# red_label.bind("<Button-1>", change_to_red)

colors = ["red","green","blue","black"]
for color in colors:
    lbl = Label(window,bg=color, width=8,height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color:globals().update(pen_color=c))

Label(text="Толщина линии").pack(side=LEFT)
wl_entry = Entry()
wl_entry.pack(side=LEFT)
wl_entry.bind("<Return>", wl_entry_bind)

wl_button = Button()
wl_button.config(text="Установить толщину", command=wl)
wl_button.pack(side=LEFT)


window.mainloop()





