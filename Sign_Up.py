from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy
from tkinter import messagebox as mb
from tkinter import *

root = Tk()
root.focus_force()
root.resizable(width=False, height=False)
root.geometry('300x300')
root.title('Sign Up')
root['bg'] = 'black'
ei = Entry(root, width=20, bg="#808080", font='arial 14')
el = Label(root, text="Enter your e-mail", width=50, height=1, bg="black", fg='white', font='arial 14')
pl = Label(root, text="Enter your password", width=50, height=1, bg="black", fg='white', font='arial 14')
pi = Entry(root, width=20, bg="#808080", font='arial 14')
cp = Label(root, text="Confirm your password", width=50, height=1, bg="black", fg='white', font='arial 14')
ci = Entry(root, width=20, bg="#808080", font='arial 14')
b = Button(root, text="Sign Up!",width=9, height=1, bg='#808080', fg='white', font='arial 14')

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
el.pack(padx=2, pady=2)
ei.pack()
pl.pack(padx=2, pady=2)
pi.pack()
cp.pack(padx=2, pady=2)
ci.pack()
b.pack(padx=20, pady=20)
b.bind('<Button-1>', leftclick)
root.mainloop()
