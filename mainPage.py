from signUpPage import login, registration
from chooseMenu import profileChoose

def starter():
    global opt
    print('Welcome to crowdFunding app')
    opt = input('you want to regisger / login ("login/reg"):  ')
    if (opt != 'login' and opt != 'reg'):
        starter()
    elif opt == 'login':
        login()
        profileChoose()
    elif opt == 'reg':
        registration()
    else:
        print('choose ("login / reg")')

starter()


    


