from tkinter import *
from tkinter import messagebox
import math

screen = Tk()
screen.title('Calculator')
screen.geometry("375x485")
screen.maxsize(width=479, height=475)
screen.minsize(width=375, height=475)
screen.configure(bg='grey')
screen.iconbitmap('cal.ico')


def click(num):
    global operator
    operator += str(num)
    text.set(operator)

def clear():
    global operator
    operator = ' '
    text.set(operator)

def equal():
    try:
        global  operator
        result = eval(operator)
        operator = str(result)
        text.set(result)
    except:
        messagebox.showinfo('Notification', 'Try again, something is wrong', parent=screen)

def cmsin():
    try:
        global operator
        result = math.sin(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again, something is wrong', parent=screen)

def cmcos():
    try:
        global operator
        result = math.cos(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again, something is wrong', parent=screen)
def cmtan():
    try:
        global operator
        result = math.tan(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again, something is wrong', parent=screen)

def cmsqrt():
    try:
        global operator
        result = math.sqrt(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again, something is wrong', parent=screen)

def cmlog():
    try:
        global operator
        result = math.log(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again, something is wrong', parent=screen)




def on_entertext_area(e):
    text_area.configure(bg='pink', fg='white')
def on_leavetext_area(e):
    text_area.configure(bg='light blue', fg='black')

def on_enter7(e):
    btn7.configure(bg='white')
def on_leave7(e):
    btn7.configure(bg='light grey')

def on_enter8(e):
    btn8.configure(bg='white')
def on_leave8(e):
    btn8.configure(bg='light grey')

def on_enter9(e):
    btn9.configure(bg='white')
def on_leave9(e):
    btn9.configure(bg='light grey')

def on_enteradd(e):
    btnadd.configure(bg='white')
def on_leaveadd(e):
    btnadd.configure(bg='light grey')

def on_enter4(e):
    btn4.configure(bg='white')
def on_leave4(e):
    btn4.configure(bg='light grey')

def on_enter5(e):
    btn5.configure(bg='white')
def on_leave5(e):
    btn5.configure(bg='light grey')

def on_enter6(e):
    btn6.configure(bg='white')
def on_leave6(e):
    btn6.configure(bg='light grey')

def on_entersub(e):
    btnsub.configure(bg='white')
def on_leavesub(e):
    btnsub.configure(bg='light grey')

def on_enter1(e):
    btn1.configure(bg='white')
def on_leave1(e):
    btn1.configure(bg='light grey')

def on_enter2(e):
    btn2.configure(bg='white')
def on_leave2(e):
    btn2.configure(bg='light grey')

def on_enter3(e):
    btn3.configure(bg='white')
def on_leave3(e):
    btn3.configure(bg='light grey')

def on_entermult(e):
    btnmult.configure(bg='white')
def on_leavemult(e):
    btnmult.configure(bg='light grey')

def on_enter0(e):
    btn0.configure(bg='white')
def on_leave0(e):
    btn0.configure(bg='light grey')

def on_enterclear(e):
    btnclear.configure(bg='white')
def on_leaveclear(e):
    btnclear.configure(bg='light grey')

def on_enterdivide(e):
    btndivide.configure(bg='white')
def on_leavedivide(e):
    btndivide.configure(bg='light grey')

def on_enterequal(e):
    btnequal.configure(bg='white')
def on_leaveequal(e):
    btnequal.configure(bg='light grey')

def on_entersin(e):
    btnsin.configure(bg='white')
def on_leavesin(e):
    btnsin.configure(bg='light grey')

def on_entercos(e):
    btncos.configure(bg='white')
def on_leavecos(e):
    btncos.configure(bg='light grey')

def on_entertan(e):
    btntan.configure(bg='white')
def on_leavetan(e):
    btntan.configure(bg='light grey')

def on_entersqrt(e):
    btnsqrt.configure(bg='white')
def on_leavesqrt(e):
    btnsqrt.configure(bg='light grey')

def on_enterlog(e):
    btnlog.configure(bg='white')
def on_leavelog(e):
    btnlog.configure(bg='light grey')


text = StringVar()
operator = ''

text_area = Entry(screen, bg='light blue',font=('arial',21, 'bold'),bd=30, justify='right', textvariable= text)
text_area.grid(row=0, columnspan=4)

btn7 = Button(screen, text='7', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(7),
              activebackground='black', activeforeground='white', bg='light grey')
btn7.grid(row=1, column=0)
btn8 = Button(screen, text='8', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(8),
              activebackground='black', activeforeground='white', bg='light grey')
btn8.grid(row=1, column=1)
btn9 = Button(screen, text='9', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(9),
              activebackground='black', activeforeground='white', bg='light grey')
btn9.grid(row=1, column=2)
btnadd = Button(screen, text='+', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click('+'),
                activebackground='black', activeforeground='white', bg='light grey')
btnadd.grid(row=1, column=3)

btn4 = Button(screen, text='4', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(4),
              activebackground='black', activeforeground='white', bg='light grey')
btn4.grid(row=2, column=0)
btn5 = Button(screen, text='5', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(5),
              activebackground='black', activeforeground='white', bg='light grey')
btn5.grid(row=2, column=1)
btn6 = Button(screen, text='6', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(6),
              activebackground='black', activeforeground='white', bg='light grey')
btn6.grid(row=2, column=2)
btnsub = Button(screen, text='-', font=('arial',18, 'bold'), bd=8, padx=18, pady=16, command=lambda : click('-'),
                activebackground='black', activeforeground='white', bg='light grey')
btnsub.grid(row=2, column=3)


btn1 = Button(screen, text='1', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(1),
              activebackground='black', activeforeground='white', bg='light grey')
btn1.grid(row=3, column=0)
btn2 = Button(screen, text='2', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(2),
              activebackground='black', activeforeground='white', bg='light grey')
btn2.grid(row=3, column=1)
btn3 = Button(screen, text='3', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(3),
              activebackground='black', activeforeground='white', bg='light grey')
btn3.grid(row=3, column=2)
btnmult = Button(screen, text='*', font=('arial',18, 'bold'), bd=8, padx=18, pady=16, command=lambda : click('*'),
                 activebackground='black', activeforeground='white', bg='light grey')
btnmult.grid(row=3, column=3)


btn0 = Button(screen, text='0', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda : click(0),
              activebackground='black', activeforeground='white', bg='light grey')
btn0.grid(row=4, column=0)
btnclear = Button(screen, text='C', font=('arial',18, 'bold'), bd=8, padx=14, pady=16, command=lambda : clear(),
                  activebackground='black', activeforeground='white', bg='light grey')
btnclear.grid(row=4, column=1)
btnequal = Button(screen, text='=', font=('arial',18, 'bold'), bd=8, padx=16, pady=16, command=lambda  : equal(),
                  activebackground='black', activeforeground='white', bg='light grey')
btnequal.grid(row=4, column=2)
btndivide = Button(screen, text='/', font=('arial',18, 'bold'), bd=8, padx=18, pady=16, command=lambda : click('/'),
                   activebackground='black', activeforeground='white', bg='light grey')
btndivide.grid(row=4, column=3)



btnsin = Button(screen, text='sin', font=('arial',16, 'bold'), bd=8, padx=17, pady=19, command=lambda : cmsin(),
              activebackground='black', activeforeground='white', bg='light grey')
btnsin.grid(row=0, column=4)
btncos = Button(screen, text='cos', font=('arial',16, 'bold'), bd=8, padx=14, pady=19, command=lambda : cmcos(),
              activebackground='black', activeforeground='white', bg='light grey')
btncos.grid(row=1, column=4)
btntan = Button(screen, text='tan', font=('arial',16, 'bold'), bd=8, padx=17, pady=19, command=lambda : cmtan(),
              activebackground='black', activeforeground='white', bg='light grey')
btntan.grid(row=2, column=4)
btnsqrt = Button(screen, text='sqrt', font=('arial',16, 'bold'), bd=8, padx=13, pady=19, command=lambda : cmsqrt(),
              activebackground='black', activeforeground='white', bg='light grey')
btnsqrt.grid(row=3, column=4)
btnlog = Button(screen, text='log', font=('arial',16, 'bold'), bd=8, padx=17, pady=19, command=lambda : cmlog(),
              activebackground='black', activeforeground='white', bg='light grey')
btnlog.grid(row=4, column=4)



text_area.bind('<Enter>',on_entertext_area)
text_area.bind('<Leave>',on_leavetext_area)

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)

btndivide.bind('<Enter>',on_enterdivide)
btndivide.bind('<Leave>',on_leavedivide)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)

btnmult.bind('<Enter>',on_entermult)
btnmult.bind('<Leave>',on_leavemult)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)


screen.mainloop()