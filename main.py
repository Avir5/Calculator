from tkinter import *
import logic
from tkinter import ttk
from tkinter import messagebox as mb



def enter_number(num):
    entry.insert(END,num)


def clear_entry():
    entry.delete(0,END)


def calc():
    second=int(entry.get())
    if operator=='+':
        res=logic.add(first, second)
    elif operator=='-':
        res=logic.substract(first, second)
    elif operator=='*':
        res=logic.multiply(first, second)
    elif operator=='/':
        res=logic.divide(first, second)
        if isinstance(res,str):
            res=''
            mb.showerror('Ошибка', 'Делить на 0 нельзя!')

    entry.delete(0,END)
    entry.insert(0,res)


def set_oper(oper):
    global operator, first
    first=int(entry.get())
    operator=oper
    entry.delete(0,END)


def validate():
    entry.text=intry.get()
    corrected_text=''.join([i for i in entry_text if i in "1234567890-"])
    if entry_text != corrected_text:
        entry.delete(0,END)
        entry.insert(0, corrected_text)


window=Tk()
window.title('КАЛЬКУЛЯТОР')


entry=ttk.Entry()
entry.grid(row=0,column=0,columnspan=4,sticky='ew')
entry.bind('<KeyRelease>', lambda event : validate())

ttk.Button(text="1",command=lambda:enter_number(1)).grid(row=1, column=0)
ttk.Button(text='2',command=lambda:enter_number(2)).grid(row=1,column=1)
ttk.Button(text='3',command=lambda:enter_number(3)).grid(row=1,column=2)

ttk.Button(text='4',command=lambda:enter_number(4)).grid(row=2,column=0)
ttk.Button(text='5',command=lambda:enter_number(5)).grid(row=2,column=1)
ttk.Button(text='6',command=lambda:enter_number(6)).grid(row=2,column=2)

ttk.Button(text='7',command=lambda:enter_number(7)).grid(row=3,column=0)
ttk.Button(text='8',command=lambda:enter_number(8)).grid(row=3,column=1)
ttk.Button(text='9',command=lambda:enter_number(9)).grid(row=3,column=2)

ttk.Button(text='0',command=lambda:enter_number(0)).grid(row=4,column=0)
ttk.Button(text='C',command=clear_entry).grid(row=4,column=1)
ttk.Button(text='=',command=calc).grid(row=4,column=2)

#кнопки для операций
ttk.Button(text='+',command=lambda:set_oper('+')).grid(row=1,column=3)
ttk.Button(text='-',command=lambda:set_oper('-')).grid(row=2,column=3)
ttk.Button(text='*',command=lambda:set_oper('*')).grid(row=3,column=3)
ttk.Button(text='/',command=lambda:set_oper('/')).grid(row=4,column=3)


window.mainloop()

'''
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Ошибка! Деление на 0."



ttk.Button(text="1", command=lambda:enter_number(1)).grid(row=1, column=0)
ttk.Button(text="2", command=lambda:enter_number(2)).grid(row=1, column=1)
ttk.Button(text="3", command=lambda:enter_number(3)).grid(row=1, column=2)

ttk.Button(text="4", command=lambda:enter_number(4)).grid(row=2, column=0)
ttk.Button(text="5", command=lambda:enter_number(5)).grid(row=2, column=1)
ttk.Button(text="6", command=lambda:enter_number(6)).grid(row=2, column=2)

ttk.Button(text="7", command=lambda:enter_number(7)).grid(row=3, column=0)
ttk.Button(text="8", command=lambda:enter_number(8)).grid(row=3, column=1)
ttk.Button(text="9", command=lambda:enter_number(9)).grid(row=3, column=2)
'''

