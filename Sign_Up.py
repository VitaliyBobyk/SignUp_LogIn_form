from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy
from tkinter import messagebox as mb
from tkinter import *

root = Tk()

root.resizable(width=False, height=False)
root.geometry('300x300')
root.title('Sign Up')
root['bg'] = 'black'
ei = Entry(root, width=40)
el = Label(root, text="Enter your e-mail", bg="black",fg='white', width=20)
pl = Label(root, text="Enter your password", bg="black",fg='white', width=20)
pi = Entry(root, width=40)
cp = Label(root, text="Confirm your password", bg="black",fg='white', width=20)
ci = Entry(root, width=40)
b = Button(root, text="Sign Up!")

def check_mail():
    email = ei.get()
    try:
        valid = validate_email(email)
        email = valid.email
        return email
    except EmailNotValidError as e:
        mb.showerror('Erorr in e-mail','The email address is not valid. It must have exactly one @-sign.')
        return None
def check_p():
    policy = PasswordPolicy.from_names(
        length=8,  # min length: 8
        uppercase=1,  # need min. 2 uppercase letters
        numbers=2,  # need min. 2 digits
        nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
    )
    password = pi.get()
    confirm_p = ci.get()
    tp = policy.test(password)
    tc = policy.test(confirm_p)
    if tp == [] and tc == []:
        mb.showinfo('Congratulations!','Well done, you have made the registration')
        return password
    else:
        return mb.showerror("Erorr password", tc)

def incl():
    vm = check_mail()
    if vm:
        vp = check_p()
        total = vm + " " + vp
        return total

def write_to_db():
    f = open('database.txt', 'a')
    par_func = incl()
    if par_func != None:
        f.write(par_func + '\n')
        f.close
        return root.destroy()

def leftclick(event):
    write_to_db()
el.pack()
ei.pack()
pl.pack()
pi.pack()
cp.pack()
ci.pack()
b.pack()
b.bind('<Button-1>', leftclick)
root.mainloop()
