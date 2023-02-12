import datetime
import time
from tkinter import CENTER, Button, Entry, Label, Tk, Toplevel

from _tkinter import TclError

root = Tk()

root.title("Секундомер")
root["bg"] = "white"
root.geometry("400x200")
root.resizable(width=False, height=False)

def end_timer(id, droot: Toplevel):
    root.after_cancel(id)
    droot.destroy

def timer(times=None, minute: Label=None, second: Label=None, start_time=None, button: Button=None, droot: Toplevel = None):
    minute.configure(text=times.minute)
    second.configure(text=times.second)
    id = None

    def inner():
        nonlocal start_time, times, id

        spend_time = time.time() - start_time
        try:
            times = (datetime.datetime.combine(datetime.date(1, 1, 1), times) - datetime.timedelta(seconds=spend_time)).time()

            minute.configure(text=times.minute)
            second.configure(text=times.second)
            start_time = time.time()

            id = root.after(1000, inner)
            button.configure(command=lambda: end_timer(id, droot))
        except OverflowError:
            try:
                end_timer(id, droot)
            except TclError:
                pass

    inner()
def start_timer():
    lminutes = minute.get()
    lseconds = second.get()

    if (lminutes != "" and lminutes != "0") or (lseconds != "" and lseconds != "0"):
        if lminutes == "":
            lminutes = 0
        if lseconds == "":
            lseconds = 0

        droot = Toplevel(root)
        droot.title("Отсчёт пошёл")
        droot["bg"] = "white"
        droot.geometry("300x150")
        droot.resizable(width=False, height=False)

        lminute = Label(droot, fg='black', justify=CENTER, font=('Arial', 20))
        lminute.place(relheight=0.4, relwidth=0.35, relx=0.1, rely=0.1)
        lsecond = Label(droot, fg='black', justify=CENTER, font=('Arial', 20))
        lsecond.place(relheight=0.4, relwidth=0.35, relx=0.55, rely=0.1)
        llabel = Label(droot, fg="black", font=('Arial', 20), text=":", bg="white")
        llabel.place(relheight=0.4, relwidth=0.1, rely=0.1, relx=0.45)
        lbutton = Button(droot, text="Остановить таймер", fg="black", bg="white", font=('Arial', 10))
        lbutton.place(relheight=0.4, relwidth=0.8, relx=0.1, rely=0.5)

        timer(datetime.time(minute=int(lminutes), second=int(lseconds)), lminute, lsecond, time.time(), lbutton, droot)

def validate(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

minute = Entry(root, fg='black', justify=CENTER, font=('Arial', 20), validate="key", validatecommand=(root.register(validate), "%S"))
minute.place(relheight=0.4, relwidth=0.35, relx=0.1, rely=0.1)
second = Entry(root, fg='black', justify=CENTER, font=('Arial', 20), validate="key", validatecommand=(root.register(validate), "%S"))
second.place(relheight=0.4, relwidth=0.35, relx=0.55, rely=0.1)
label = Label(root, fg="black", font=('Arial', 20), text=":", bg="white")
label.place(relheight=0.4, relwidth=0.1, rely=0.1, relx=0.45)
button = Button(root, text="Запустить таймер", fg="black", bg="white", font=('Arial', 10), command=start_timer)
button.place(relheight=0.4, relwidth=0.8, relx=0.1, rely=0.5)

root.mainloop()