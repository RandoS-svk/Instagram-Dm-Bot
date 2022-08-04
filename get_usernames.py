import instaloader

instagram_data = instaloader.Instaloader()
# Login or load session
username = input('Enter Username: ')
password = input('Enter Password: ')
limit_users = input('Limit of users: ')
limit_users_correct = False
is_logged_in = False
while limit_users_correct == False:
    try: 
        limit_users = int(limit_users)
    except:
        limit_users = input('Limit of users: ')
    else:
        limit_users_correct = True

while is_logged_in == False:
    try:
        login_info = instagram_data.login(username, password)        # (login)
    except:
        print('Bad password try it again')
        username = input('Enter Username: ')
        password = input('Enter Password: ')
    else:
        is_logged_in = True
        print('you are logged in')

profile = instaloader.Profile.from_username(instagram_data.context, username)
follow_list = []
count=0

file = open("usernames.txt", "w")
file.close()
for follower in profile.get_followers():
    follow_list.append(follower.username)    
    file = open("usernames.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
    if count == limit_users:
        break



