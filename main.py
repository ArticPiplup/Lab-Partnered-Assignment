
def encode_password(password):
    encoded_password = []
    for char in password:
        encoded_password.append(str(int(char) + 3))
    return "".join(encoded_password)
def decoded_password(input_string):
    result_string = ""
    for char in input_string:
        if char.isdigit():
            new_char = str((int(char) - 3) % 10)
            result_string += new_char
        else:
            result_string += char
    print("Decoded Password:", result_string)
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
            encoded_password = encode_password(str(input("Enter your password to be encoded: ")))
            print(encoded_password)
        elif menu_option == 2:
            decoded_password(encoded_password)
            pass
        else:
            print("Please choose a valid option")

main()

