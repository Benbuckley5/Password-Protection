def password():
    count = 1
    while count <= 10:
        key = input(f'please input password ({count}/10): ')
        if key == 'password':
            print('Access Granted')
            break
        else:
            print('Access Denied :(')
            count +=1
    if count == 11:
        print('system locked :(')
    else:
        print('system unlocked!')

password()