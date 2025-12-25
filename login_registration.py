import re
import os 

FILE_NAME = "users.txt"


# -------------- USERNAME VALIDATION -------------
def validate_username(username):
    if "@" not in username or "." not in username:
        return False 
    if not username[0].isalpha():
        return False 
    if username.index("@") > username.rindex("."):
        return False
    if username[username.index("@") + 1] == ".":
        return False
    return True

#----------------- PASSWORD VALIDATION -----------

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%!&*]", password):
        return False
    return True

#----------------- REGISTER USER -----------

def register():
    username = input("Enter Email ID: ")
    password = input("Enter Password: ")
     
    if not validate_username(username):
        print(" Invalid Email format")
        return
    if not validate_password(password):
        print(" Invalid password format")
        return

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if ":" not in line:
                    continue
                stored_user = line.split(":")[0]
                if stored_user == username:
                    print(" User already exists")
                    return
    with open(FILE_NAME, "a") as file:
        file.write(f"{username}:{password}\n")
    
    print(" Registration sucessfull")


# ---------- LOGIN USER -----------------
    
def login():
    username = input("Enter Email ID: ")
    password = input("Enter Password: ")
    
    if not os.path.exists(FILE_NAME):
        print(" No users found. Please register.")
        return
    with open(FILE_NAME, "r") as file:
        for line in file:
            try:
                stored_user, stored_pass = line.strip().split(":")
            except ValueError:
                continue
            if stored_user == username and stored_pass == password:
                print(" Login successful")
                return

    print(" Invalid credentials")
    choice = input("1. Register 2. Forgot Password : ")
    if choice == "1":
        register()
    elif choice == "2":
        forgot_password()


#----------- FORGOT PASSWORD ----------------

def forgot_password():
    username = input("Enter your Email ID: ")

    if not os.path.exists(FILE_NAME):
        print(" No users found. Please register.")
        return
    
    found = False
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            try:
                stored_user, _ = line.strip().split(":")
            except ValueError:
                file.write(line)
                continue
            if stored_user == username:
                found = True
                while True:
                  new_password = input("Enter new password: ")
                  
                  if validate_password(new_password):
                    file.write(f"{username}:{new_password}\n")
                    print("Password updated successfully")
                    break
                  else:
                    print("Invalid password format. Try again")
            else:
                file.write(line)

    if not found:
            print("Email ID not found. Please register.")


# ----------------- MAIN MENU --------------

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")
         
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you")
            break 
        else:
            print(" Invalid choice")


main()

    