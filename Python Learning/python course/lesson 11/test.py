app_theme = 'light'
user_status = 'guest'

def display_current_settings():
    session_id = 1234
    print(f'app theme:{app_theme} \nuser status:{user_status} \nsession id:{session_id} \n')

def change_theme(newtheme):
    global app_theme
    app_theme = newtheme
    print('global theme changed!')

def login_user():
    user_status = 'admin'
    print(f'inside function user_status is: {user_status} \n')


display_current_settings()
change_theme('Dark')
login_user()