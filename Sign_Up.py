from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy

def check_mail():
    email = str(input('Enter your e-mail: '))
    try:
        valid = validate_email(email)
        email = valid.email
        return email
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        print(email)
def check_p():
    policy = PasswordPolicy.from_names(
        length=8,  # min length: 8
        uppercase=1,  # need min. 2 uppercase letters
        numbers=2,  # need min. 2 digits
        nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
    )
    password = str(input('Enter your password: '))
    while policy.test(password) != []:
        print(policy.test(password))
        password = str(input('Enter your password: '))
    if policy.test(password) == []:
        confirm_p = str(input('Confirm your password: '))
    if password == confirm_p:
        print('Well done, you have made the registration')
        return password
    while password != confirm_p:
        print("Password's not the same")
        confirm_p = str(input('Confirm your password: '))
        if password == confirm_p:
            print('Well done, you have made the registration')
            return password
        return password
    return password

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

write_to_db()
