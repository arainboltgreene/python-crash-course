# 5-8 hello admin

usernames = ['admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + " thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-9 No User

# 5-10 checking usernames
print("\n5-10 Checking Usernames")
current_users = ['user1', 'user2', 'user3', 'user4', 'user5']

new_users = ['user1', 'user2', 'newuser3', 'newuser4', 'newuser5']

for new_user in new_users:
    if new_user in current_users:
        print("That username is already taken, please choose another.")
    else:
        print("That username is available.")

# 5-11 Ordinal Numbers
print("\n5-11 Ordinal Numbers")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
