username = ("python")
password = ("rules")
attempts= 0
max_attempts = 5
while attempts<max_attempts:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    if input_username == username and input_password == password:
        print("Welcome")
        break
    else:
        print("Wrong username or password")
    attempts+=1
    if attempts == max_attempts:
        print("Acces denied")

