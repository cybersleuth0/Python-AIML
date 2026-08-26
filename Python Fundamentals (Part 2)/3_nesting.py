username=input("Enter your username: ")
password=input("Enter your password: ")

if username=="admin" and password=="admin123":
    print("Login successful")
else:
    if username!="admin":
        print("Invalid username")
    if password!="admin123":
        print("Invalid password")
