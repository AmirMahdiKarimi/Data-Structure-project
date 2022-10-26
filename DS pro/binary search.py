from tkinter import *
import tkinter.messagebox


def win(w):
    w.title("Binary Search")
    w.geometry("400x250")
    w.resizable(width=False, height=False)
    w.configure(bg="#48DED5")


win1 = Tk()
win(win1)

n_inp = StringVar()
show_msg = StringVar()
numbers = list()
n = 0
cnt = 0

lbl1 = Label(win1, text="How many number are there in the array ?", font=("Segoe UI Semibold", 12), width=400, height=4,
             bg="#48DED5")
lbl1.pack(side=TOP, padx=5, pady=5)

Entry_n = Entry(win1, textvariable=n_inp, font=("Segoe UI Semibold", 14), width=8)
Entry_n.pack(side=TOP, padx=5)

n_btn = Button(win1, text="submit", width=12, height=2, bg="#D5CABD", command=lambda: get_n(), cursor="hand2")
n_btn.pack(side=TOP, padx=2, pady=20)


def get_n():
    global n
    try:
        n = int(n_inp.get())
        win1.destroy()
        get_nums()
    except:
        tkinter.messagebox.showerror("ERROR", "Enter a number!")


def get_nums():
    global cnt
    if cnt == n:
        print(numbers)
        numbers.sort()
        question()
    else:
        cnt += 1
        win2 = Tk()
        win(win2)
        number = StringVar()
        lbl2 = Label(win2, text=f"Enter {cnt} st item :", font=("Segoe UI Semibold", 12), width=400, height=4, bg="#48DED5")
        lbl2.pack(side=TOP, padx=5, pady=5)

        Entry_num = Entry(win2, textvariable=number, font=("Segoe UI Semibold", 14), width=8)
        Entry_num.pack(side=TOP, padx=5)

        num_btn = Button(win2, text="submit item", width=12, height=2, bg="#D5CABD",
                         command=lambda: add_num(int(number.get()), win2),
                         cursor="hand2")
        num_btn.pack(side=TOP, padx=2, pady=20)
        win2.mainloop()


def add_num(num, win2):
    try:
        numbers.append(num)
        win2.destroy()
        get_nums()
    except:
        tkinter.messagebox.showerror("ERROR", "Enter a number!")


def question():
    win3 = Tk()
    win(win3)
    win3.geometry("400x350")

    number = StringVar()
    res = StringVar()
    lbl3 = Label(win3, text="What number are you looking for ?", font=("Segoe UI Semibold", 12), width=400, height=4,
                 bg="#48DED5")
    lbl3.pack(side=TOP, padx=5, pady=5)

    Entry_num = Entry(win3, textvariable=number, font=("Segoe UI Semibold", 14), width=8)
    Entry_num.pack(side=TOP, padx=5)

    num_btn = Button(win3, text="submit", width=12, height=2, bg="#D5CABD",
                     command=lambda: res.set(BinarySearch(numbers, n, int(number.get()))),
                     cursor="hand2")
    num_btn.pack(side=TOP, padx=2, pady=20)

    lbl4 = Label(win3, textvariable=res, font=("Segoe UI Semibold", 12), width=400, height=4,
                 bg="#48DED5")
    lbl4.pack(side=TOP, padx=5, pady=5)

    win3.mainloop()


def BinarySearch(numbers, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = int((low + high) / 2)
        if numbers[mid] == x:
            return f"{x} is in the array."
        elif numbers[mid] < x:
            low = mid + 1
        elif numbers[mid] > x:
            high = mid - 1
    return f"{x} is not in the array."


win1.mainloop()
