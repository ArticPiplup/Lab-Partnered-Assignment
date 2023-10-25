
def encode_password(password):
    encoded_password = []
    for char in password:
        encoded_password.append(str(int(char) + 3))
    return "".join(encoded_password)
def menu_printer():
    print('''
    Menu
    -------------
    1. Encode
    2. Decode
    3. Quit
    ''')


def main():
    menu_option = 0
    while menu_option != 3:
        menu_printer()
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            print(encode_password(str(input("Enter your password to be encoded: "))))
        elif menu_option == 2:
            # decode_password(encoded_password)
            pass
        else:
            print("Please choose a valid option")

main()

