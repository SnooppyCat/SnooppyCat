import tkinter
import random
from tkinter import *
from random import randint
from os import remove
from distutils import command

print('Logs terminal:')

def generator(amount, port=''):
    prc_bfr=0
    for n in range(amount):
        a = randint(0,255)
        b = randint(0,255)
        c = randint(0,255)
        d = randint(0,255)
        f = open('ip-addresses.txt', 'a', encoding='utf-8')
        f.write(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+port+'\n')
        f.close()
        
        prc = int(n//(amount/100))
        
        if(prc!=prc_bfr):
            print(str(prc)+'%')
        prc_bfr = prc        
    print('Success!')

    notif("IP-адреса успешно сгенерированы и записаны в\nip-addresses.txt")
    
def notif(value):
    output.delete("0.0","end")
    output.insert("0.0",value)

def handler():
    try:
        amount = int(entry_amount.get())
        if var1.get() == 1:
            port = ':'+str(int(entry_port.get()))
            generator(amount, port)
        else:
            generator(amount)
    except ValueError:
        notif("Невозможно определить количество/порт")

def delete():
    try:
        remove('ip-addresses.txt')
        notif("Файл ip-addresses.txt успешно удален")
    except:
        notif("Невозможно удалить несуществующий файл")

def lock():
    if var1.get() == 1:
        entry_port.configure(state=NORMAL)
    elif var1.get() == 0:
        entry_port.configure(state=DISABLED)
        
root = Tk()
root.title('Generator from sirota')

label1=Label(root, text="Генератор ip-адресов")
label1.grid()

frame = Frame(root)
frame.grid()

label2=Label(frame, text='Количество:')
label2.grid(row=1,column=1)

entry_amount = Entry(frame, width=4, borderwidth=5)
entry_amount.grid(row=1,column=2)


button1 = Button(frame, text="Сгенерировать", command=handler)
button1.grid(row=1, column=3, padx=(10,0))

button2 = Button(frame, text="Удалить файл", command=delete)
button2.grid(row=1, column=4, padx=(10,0))

label2=Label(frame, text='Указать порт:')
label2.grid(row=2,column=1)

entry_port = Entry(frame, width=4, borderwidth=5, state=DISABLED)
entry_port.grid(row=2,column=2)

var1 = IntVar()

check_port1 = Radiobutton(frame, text='С портами', variable = var1, value=1, command=lock)
check_port1.grid(row=2,column=3)
check_port2 = Radiobutton(frame, text="Без портов", variable = var1, value=0, command=lock)
check_port2.grid(row=2,column=4)

output = Text(frame, bg="lightblue", font="Arial 9", width=45, height=3)
output.grid(row=3, columnspan=8)

root.mainloop()