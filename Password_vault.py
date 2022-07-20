
from cryptography.fernet import Fernet
from json import loads, dumps
import os

def main():
    key = bytes(b'qG3o2lV-nlJyKdQhdwrA-luHI7dQVX-Hbj0ovMvyuek=')
    data = decrypt(key)
    options = ['Login','Add User','remove user']
    for f in options:
        print(f)
    user = input(':')
    try:
        if user == 'add user':
            add_user(data)
            save(key,data)
        if user == 'remove user':
            remove_user(data)
            save(key,data)
        if user == 'login':
            stuff = login(data)
            if stuff[0] == True:
                os.system("cls")
                data = user_choice(data,stuff[1])
                save(key,data)
            else:
                print('Wrong username or password')
    except KeyError:
        print ("That does account does not exitst.")
    finally:
        save(key,data)
    

def save(key,data):
    with open ('passwords.txt','wb') as doc:
        dump = dumps(data)
        fernet = Fernet(key)
        encMessage = fernet.encrypt(dump.encode())
        doc.write(encMessage)

def decrypt(key):
    with open ('passwords.txt','rb') as doc:
        for n in doc:
            file =  n
        fernet = Fernet(key)
        data = fernet.decrypt(file).decode()
        data = loads(data)
        return data

def login(data):
    os.system("cls")
    username = input('Username: ')
    password = input ('Password: ')
    if data[username]['login']['username'] == username and data[username]['login']['password'] == password:
        return True,username

def add_account(data,other):
    os.system("cls")
    name = input('What is the name of the account? ')
    username = input('What is your username? ')
    password = input('What is your password? ')
    enter = [username,password]
    data[other]['accounts'][name] = enter
    print(f'''Your account has been added
{name}: username:{username}, password:{password}''')

def remove_account(data,other):
    os.system("cls")
    print(data)
    for f in data[other]['accounts']:
        print(f)
    remove = input('Which accounts do you want to remove? ')
    del data[other]['accounts'][remove]
    print(f'{remove} has been removed')

def user_choice(data,other):
    while 1:
        options = ['view account', 'add account','remove account','change login','exit']
        for t in options:
            print(t)
        user = input(':')
        if user not in options:
            print('That is not one of the options.')
        if user == 'add account':
            add_account(data,other)
            os.system("cls")
        elif user == 'remove account':
            remove_account(data,other)
            os.system("cls")
        elif user == 'view account':
            view_account(data,other)
            os.system("cls")
        elif user == 'change login':
            change_login(data,other)
            os.system("cls")
        elif user == 'new file' and data[other] == data['admin']:
             data = new_file(data)
             os.system("cls")
        elif user == 'exit':
            break
        

    return data

def change_login(data,other):
    old_username = input('Old username: ')
    old_password = input('Old password: ')
    new_username = input('New username: ')
    new_password =  input('New password: ')
    if old_username == data['user']['username'] and old_password == data['user']['password']:
        data[other]['login']['username'] = new_username
        data[other]['login']['password'] = new_password
        print('Username and password changed.')
    else:
        print('Username and password change canceled.')

def view_account(data,other):
    os.system("cls")
    for f in data[other]['accounts']:
        print(f)
    user = input('Select an account: ')
    os.system("cls")
    stuff = data[other]['accounts'][user]
    print(f'''Account: {user}
Username: {stuff[0]}
Password: {stuff[1]}
    ''')
    input("Press enter to continue. ")

def new_file(data):
    data = {
        'admin':{
            'login':{
                'username':'admin',
                'password':'root'
            },
            'accounts':{
                'google':['username','password']
            }

        }
    }
    print('file has been restord')
    return data
    

def add_user(data):
    os.system("cls")
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    other = {'login':{'username':username,'password':password},'accounts':{}}
    data[username] = other
    print('User has been added')

def remove_user(data):
    os.system("cls")
    for f in data:
        print(f)
    input('What user do you want to remove: ')
    stuff = login(data)
    if stuff[0] == True:
        del data[stuff[1]]


if __name__ == '__main__':
    main()