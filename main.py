print ("We are starting with Git")
print("Second line")

print ("Third print")


users = {
    'admin': {'password': 'adm1n'},
    'man': {'password': 'thing'},
    'cool': {'password': 'guy'}
}

while True:
    user_input = input('Enter your username: ')

    if user_input in users:
        password = input('Enter the password: ')

        if password == users[user_input]['password']:
            print('Welcome')
        else:
            print('The password you have entered is incorrect')
            continue
    else:
        print('The username does not exist')
        continue
    break