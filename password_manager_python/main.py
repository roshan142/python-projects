#4/4/2024 Basic Password Manager
from cryptography.fernet import Fernet

def load_key():
    file =  open('key.key',"rb")
    key = file.read()
    file.close()
    return key
'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key',"wb") as key_file:
        key_file.write(key)
write_key()'''

#master_pwd = input("What is the master password? :")
key = load_key() #+ master_pwd.encode()
fer = Fernet(key)

def add():
    name = input("Account Name:")
    pwd = input("Password:")
    with open('passwords.txt','a') as file:
        file.write( name + '|' + fer.encrypt(pwd.encode()).decode()  + '\n')

def view():
    with open('passwords.txt','r') as file:
        for i in file.readlines():
            data = i.rstrip()
            user,passwd = data.split("|")
            print("User:",user, "| Password: ",fer.decrypt(passwd.encode()).decode())

while True:
    mode = input("Would you like to add a new password or view existing ones or press q to quit (view,add,q) :")
    if mode == 'q':
        quit()
    if mode == "view":
       view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
















































