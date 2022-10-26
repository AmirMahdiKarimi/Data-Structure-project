from tkinter import *
import tkinter.messagebox

win = Tk()
win.title("Postfix to Prefix")
win.geometry("400x250")
win.resizable(width=False, height=False)
win.configure(bg="#48DED5")

frm1 = Frame(win, width=400, height=200, bg="#48DED5")
frm1.pack(side=TOP)

frm2 = Frame(win, width=400, height=100, bg="#48DED5")
frm2.pack(side=TOP)

frm3 = Frame(win, width=400, height=200, bg="#48DED5")
frm3.pack(side=TOP)

post = StringVar()
pre = StringVar()
operations = ["+", "-", "*", "/", "^"]

lbl_1 = Label(frm1, text="Postfix :", font=(1), bg='#48DED5')
lbl_1.pack(side=LEFT, padx=10, pady=30)

inp_1 = Entry(frm1, textvariable=post, font=(18))
inp_1.pack(side=LEFT, padx=10, pady=10)

lbl_res = Label(frm3, text="Prefix :", font=(10), bg='#48DED5')
lbl_res.pack(side=LEFT, padx=10, pady=30)

output = Entry(frm3, textvariable=pre, font=(18))
output.pack(side=LEFT, padx=10, pady=20)


def ToPrefix(postfix, operations):
    pre_stack = []
    for char in postfix:
        if char in operations:
            if len(pre_stack) < 2:
                tkinter.messagebox.showerror("ERROR", "This phrase is not postfix or is wrong.")
            else:
                sec = pre_stack.pop()
                fir = pre_stack.pop()
                pre_stack.append(char + fir + sec)
        else:
            pre_stack.append(char)
    if len(pre_stack) > 1:
        tkinter.messagebox.showerror("ERROR", "This phrase is not postfix or is wrong.")
    else:
        pre.set(pre_stack.pop())


PostToPre_btn = Button(frm2, text="Postfix to Prefix", width=14, height=2, bg="#D5CABD",
                       command=lambda: ToPrefix(post.get(), operations), cursor="hand2")
PostToPre_btn.pack(side=RIGHT, padx=2, pady=3)

win.mainloop()
