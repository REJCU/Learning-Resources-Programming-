while True:
    print("enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("error")

while True:
    password = input("New Password: ")
    if password.isalnum():
        break
    print('error')
