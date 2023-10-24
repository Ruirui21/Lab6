def encode(password):
    newpassword = ""
    for i in range(8):
        newpassword = newpassword + str((int(password[i]) + 3) % 10)
    return newpassword


def decode_password(newpassword):   # <-- Decode funct by Jenian Exum
    decoded_password = ""
    for digit in newpassword:
        decoded_password += str((int(digit) - 3) % 10)
    return decoded_password


if __name__ == "__main__":
    while True:
        print("Encoder menu")
        print("0. Quit")
        print("1. Encode Password")
        print("2. Decode Password")
        menu_option = input("Select a Menu Option: ")
        if menu_option == "0":
            break
        elif menu_option == "1":
            password = input("Enter a password to encode: ")
            print("Your encoded password is " + encode(password))
        elif menu_option == "2":
            return_pass = decode_password(encode(password))
            print("The decoded password is " + return_pass)
