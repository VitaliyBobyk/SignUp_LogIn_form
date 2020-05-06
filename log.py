from tkinter import messagebox as mb
from tkinter import *
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

b = Button(root, text="Log In!!", width=9, height=1, bg='#808080', fg='white', font='arial 14')

def finish():
    log_in = ei.get()
    password = pi.get()
    ind_l = 0
    for i in list_db:
        if i == log_in:
            ind_l = list_db.index(i)
        if i == log_in  == log_in and list_db[ind_l + 1] == password:
            f.close()
            mb.showinfo('Congratulations!','You have successfully logged in!')
            return root.destroy()
    f.close()
    mb.showerror('Eroor!!','Login or password incorrect!')

def leftclick(event):
    finish()
el.pack(padx=5, pady=5)
ei.pack()
pl.pack(padx=5, pady=5)
pi.pack()
b.pack(padx=20, pady=20)
b.bind('<Button-1>', leftclick)
root.mainloop()
