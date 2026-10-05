from tkinter import *
from tkinter import messagebox as mb

def check():
    global s1
    global s2
    global s3
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен

def mult():
    check()
    global s1
    global s2
    global s3
    slag1 = int(s1)
    slag2 = int(s2)
    slag3 = int(s3)
    summa = slag1 * slag2 * slag3
    m1['text'] = f"{s1} * {s2} * {s3} = {str(summa)}"

    answer = mb.askretrycancel(title="Вопрос", message="Умножить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

def summ():
    check()
    global s1
    global s2
    global s3
    slag1 = int(s1)
    slag2 = int(s2)
    slag3 = int(s3)
    summa = slag1 + slag2 + slag3
    m1['text'] = f"{s1} + {s2} + {s3} = {str(summa)}"

    answer = mb.askretrycancel(title="Вопрос", message="Сложить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

window = Tk()
window.title("Калькулятор")
m = Label(height=3, text="Введите три числа и нажмите на кнопку для вычисления суммы")
m.pack()
e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()  # Добавление третьего поля для ввода
e3.pack()

s1 = e1.get()
s2 = e2.get()
s3 = e3.get()

b = Button(text="Сложить три числа", command=summ)
b.pack()
b2 = Button(text="Умножить три числа", command=mult)
b2.pack()
m1 = Label(height=3)
m1.pack()




window.mainloop()