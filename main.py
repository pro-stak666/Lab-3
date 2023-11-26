import tkinter as tk
from tkinter import messagebox
import random

ALPHABET = list('QWERTYUIOPASDFGHJKLZXCVBNM')


def check(n):
    if len(n) == 6 and all([i.isdigit() for i in n]):
        return True
    return False


def generate_key():
    n = arg_A.get()
    if check(n):
        first_block = list(n[3:]) + random.choices(ALPHABET, k=2)
        second_block = list(n[:3]) + random.choices(ALPHABET, k=2)
        random.shuffle(first_block)
        random.shuffle(second_block)
        third_block = str(int(''.join((filter(lambda x: x.isdigit(), first_block)))) + int(
            ''.join((filter(lambda x: x.isdigit(), second_block))))).rjust(4, '0')
        res_arg.configure(text=f"{''.join(first_block)}-{''.join(second_block)} {third_block}")
    else:
        tk.messagebox.showwarning('Ошибка', 'Число не удовлетворяет условиям!')


def close():
    window.destroy()


window = tk.Tk()
window.geometry('1000x800')
bg_img = tk.PhotoImage(file='cm.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_A = tk.Label(frame, text='Введите 6-ти значное число', font=('Arial', 30))
lbl_A.grid(column=1, row=1, padx=10, pady=15)
arg_A = tk.Entry(frame, width=10)
arg_A.grid(column=1, row=2, padx=10, pady=15)

res_arg = tk.Label(frame, width=20)
res_arg.grid(column=1, row=3)

btn_calc = tk.Button(frame, text='сгенерировать ключ', command=generate_key)
btn_calc.grid(column=0, row=3, padx=10, pady=15)
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=2, row=3, padx=10, pady=15)

window.mainloop()
