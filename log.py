from tkinter import messagebox as mb
from tkinter import *
f = open('database.txt')
s = f.read()
list_db = s.split()

root = Tk()
root.resizable(width=False, height=False)
root.geometry('300x300')
root.title('Sign Up')
root['bg'] = 'black'
ei = Entry(root, width=40)
el = Label(root, text="Enter your e-mail", bg="black",fg='white', width=20)
pl = Label(root, text="Enter your password", bg="black",fg='white', width=20)
pi = Entry(root, width=40)
b = Button(root, text="Log In!!")

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
el.pack()
ei.pack()
pl.pack()
pi.pack()
b.pack()
b.bind('<Button-1>', leftclick)
root.mainloop()
