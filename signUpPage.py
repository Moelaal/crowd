
import re
from chooseMenu import profileChoose


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def registration():
    usrdata = open('userData.txt','r')
    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ')
    email = input('Enter your Email: ')
    phoneNum = input('Enter you phone number: ')
    password = input('Enter your password: ')
    confPassword = input('confirm your password: ')
    
    r =[]
    n = []
    for i in usrdata:
        a,b = i.split(',')
        b = b.strip()
        r.append(a)
        n.append(b)
    mydata = dict(zip(r, n))


    if password != confPassword:
        print('password not the same')
        registration()
    if not re.fullmatch(regex, email):
        print('Enter vaild email')
        registration()
    if len(phoneNum) < 10:
        if not re.match("^01[0125][0-9]{8}$", phoneNum):
            print('enter vaild phone number')
            registration()
    else:
        if len(password) < 6:
            print('short password')
            registration()
        else:
            usrdata = open('userData.txt','a')
            usrdata.write(email + ',' + password + '\n')
            print('Great you created your account successfully!')




def login():
    usrData = open('userData.txt','r')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    r =[]
    n = []
    for i in usrData:
        a,b = i.split(',')
        b = b.strip()
        r.append(a)
        n.append(b)
    mydata = dict(zip(r, n))

    try:
        if mydata[email]:
            try:
                if password == mydata[email]:
                    print('Login successfully')
                    print(f'you logged with email, {email}')
                    # profileChoose()
                else:
                    print('Or password or email is wrong')
            except:
                print('Wrong password or email, Try again')
        else:
            print('Wrong password or email')
    except:
        print('Email or password wrong')