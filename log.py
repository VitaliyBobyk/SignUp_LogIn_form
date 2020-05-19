from tkinter import messagebox as mb
from tkinter import *
import sqlite3 as sq


con = sq.connect('saper.db')
cursor = con.cursor()
cursor.execute('SELECT * FROM users')
names = list(map(lambda x: x, cursor.fetchall()))
for i in names:
    if i[0] == 'jjasjdhjs@mail.com':
        print(i[0])
# print(names[0])


f = open('database.txt')
s = f.read()
list_db = s.split()

root = Tk()
root.focus_force()

root.resizable(width=False, height=False)
root.geometry('300x300')
root.title('Log In')
root['bg'] = 'black'

ei = Entry(root, width=20, bg="#808080", font='arial 14')
el = Label(root, text="Enter your e-mail", width=50, height=1, bg="black", fg='white', font='arial 14')

pl = Label(root, text="Enter your password", width=50, height=1, bg="black", fg='white', font='arial 14')
pi = Entry(root, width=20, bg="#808080", font='arial 14')

b = Button(root, text="Log In!!", width=9, height=1, bg='#808080', fg='black', font='arial 14')

def leftclick(event):
    log_in = ei.get()
    password = pi.get()
    cursor.execute('SELECT * FROM users')
    names = list(map(lambda x: x, cursor.fetchall()))
    for i in names:
        if i[0] == log_in :
            if i[1] == password:
                mb.showinfo('Congratulations!', 'Hello, ' + i[0] +'\nYou have successfully logged in!')
                return root.destroy()
            else:
                return mb.showerror('Erorr!', 'Incorrect Login or Password')
        else:
            continue
    return mb.showerror('Erorr!', 'User not exist!')

el.pack(padx=5, pady=5)
ei.pack()
pl.pack(padx=5, pady=5)
pi.pack()
b.pack(padx=20, pady=20)
b.bind('<Button-1>', leftclick)
root.mainloop()
