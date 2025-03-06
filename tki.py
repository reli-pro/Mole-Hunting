import tkinter as tk
from tkinter import ttk


class new():
    def text(fr, t_s, wid=None, hei=None, bg=None, x=None, y=None, m=0, fnt=None):
        text = tk.Text(fr, bg=bg, height=hei, width=wid, font=(fnt, t_s))
        if m == 0:
            text.pack()
        
        elif m == 1:
            text.place(x=x, y=y)

        return text


def label(t_s, t, f, m=0, fnt=None, x=None, y=None, tag=None, anchor=tk.CENTER, width=None, height=None):
    label = tk.Label(f, text=t, tag=tag, font=(fnt,t_s), anchor=anchor, width=width, height=height)
    if m == 1:
        label.place(x=x, y=y)
    elif m == 0:
        label.pack()

    return label


def button(f, t_s, t, c=None, x=None, y=None, m=0, wid=None, hei=None, anc=tk.CENTER):
    button = tk.Button(f, text=t, font=(None,t_s), command=c, width=wid, height=hei, anchor=anc)

    if m == 1:
        button.place(x=x, y=y)
    
    elif m == 0:
        button.pack()

    return button


def combobox(f, t_s, s, v, x, y, h, w, fnt=None):
    combobox = ttk.Combobox(f, font=(fnt,t_s), values=v, state=s)
    combobox.place(x=x, y=y, height=h, width=w)

    return combobox


def frame(w, h, bg=None):
    frame = tk.Frame(width=w, height=h, bg=bg)

    return frame


def entry(f, x, y, h, w, t_s, fnt=None):
    entry = tk.Entry(f, font=(fnt,t_s))
    entry.place(x=x, y=y, height=h, width=w)

    return entry


def frame(w, h):
    frame = tk.Frame(width=w, height=h)

    return frame


def create_canvas(f, w, h, b="white", m=0, x=None, y=None):
    canvas = tk.Canvas(f, width=w, height=h, bg=b)

    if m == 1:
        canvas.place(x=x, y=y)
    else:
        canvas.pack()

    return canvas


def pic(canvas, Path, x, y, tag):
    img = tk.PhotoImage(file=Path)
    canvas.create_image(x, y, image=img, tag=tag)

    return img

def menu(master):
    menu = tk.Menu(master)
    master["menu"] = menu
    master.config(menu=menu)

    return menu