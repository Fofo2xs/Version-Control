
#Sephora Pierre-Louis

def encode(password):
    password_list = list(password)
    encoded_list = []
    for item in password_list:
        item = int(item)
        item += 3
        encoded_list.append(str(item))

    encoded_string = ''.join(encoded_list)

    return encoded_string

def decode(password):
    decoded_password = ""
    for x in password:
        decoded_password += str((int(x)+7)%10)
    return decoded_password

def main():
    while True:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option =  int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter a password to encode: ")
            print("Your password has been encoded and stored!")
            password_encoded = encode(password)

        elif option == 2:
            print("The encoded password is " + password_encoded  + ", and the original password is "
                  + decode(password_encoded) + ".")

        elif option == 3:
            break
        print()

if __name__ == '__main__':

    main()



