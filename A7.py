####including the bouns ######

import re
def UserData():
    name = raw_input("please enter your name: ")
    while True:
        if not name:
            print "you didn't enter a name value"
            break
        else:
            email = raw_input("please enter your email: ")
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' #bouns
            if (re.search(regex,email)):
                print "please check your following data: "
                print (name, email)
                break
            else:
                print" You entered invalid email"
UserData()

    