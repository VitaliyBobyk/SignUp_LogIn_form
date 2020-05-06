from tkinter import *



root = Tk()

root.resizable(width=False, height=False)
root.geometry('300x300')
root.title('Hello!')
root['bg'] = 'black'

el = Label(root, text="What do you want to Do?", width=50, height=1, bg="black", fg='white', font='arial 14')

b1 = Button(root, text="Sign Up!", width=9, height=1, bg='#808080', fg='white', font='arial 14')

b2 = Button(root, text="Log In!", width=9, height=1, bg='#808080', fg='white', font='arial 14')


def leftclick1(event):
    root.destroy()
    import Sign_Up
def leftclick2(event):
    root.destroy()
    import log


    print('log')

el.pack()
b1.pack(padx=20, pady=20)
b2.pack()
b1.bind('<Button-1>', leftclick1)
b2.bind('<Button-1>', leftclick2)
root.mainloop()