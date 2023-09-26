authfile = open("Authentication.txt", "w")

file = open("username.txt", "w")
notes = []
while True:
  choice = int(input("Press 1 for sign up Press 2 for log in "))
  if choice == 1:
    print("Sign Up First")
    username_1 = input("Create Your user name here:")
    password_1 = input("Create Your password here:")
    signup = username_1 + password_1
    authfile = open("Authentication .txt", "w")
    authfile.write(signup)
    authfile.close()
  else:
    print("now sign in:")
    username = input("Put your user name here:")
    password = input("Put your password here:")
    sign_in = username + password
    loginfile = open("Authentication.txt", "r")
    cred = loginfile.read()
    print("Confirm:",sign_in,cred)
    if sign_in == cred:
      options=int(input("Press 1 to read notes\nPress 2 to write notes  "))
      if options==2:
        datafile = open("notes.txt", "w")
        notes = input("Put Notes Here:")
        datafile.write(notes)
        datafile.close()
      else:
        datafile = open("notes.txt", "r")
        info=datafile.read()
        print(info)
        datafile.close()
    else:
      print("Password is not correct")
      logout = int(input("Press 1 To Stay Or Press 2 To Sign Out"))
      if logout == 2:
        break
