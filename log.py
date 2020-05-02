f = open('database.txt')
s = f.read()
list_db = s.split()

log_in = str(input('Enter your e-mail: '))
password = str(input('Enter your password: '))

for i in list_db:
    if i == log_in:
        ind_l = list_db.index(i)
        if list_db[ind_l + 1] == password:
            print('You have successfully logged in!')
        else:
            print('Login or password incorrect')



f.close()
