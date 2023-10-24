def encode(password):
    newpassword=""
    for i in range(8):
        newpassword=newpassword+str((int(password[i])+3)%10)
    return newpassword
if __name__=="__main__":
    while(True):
        print("Encoder menu")
        print("0. Quit")
        print("1. Encode Password")
        print("2. Decode Password")
        menu_option=input("Select a Menu Option: ")
        if menu_option=="0":
            break
        elif menu_option=="1":
            password=input("Enter a password to encode: ")
            print("Your encoded password is "+encode(password))
