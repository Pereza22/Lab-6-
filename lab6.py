# Angel Perez; Partner: Gregory Rodriguez - Lab 6

# function that encodes password and checks if password is 8-digits
def encode_password(password):
    if len(password) != 8 or not password.isdigit():
        return "Invalid password format"
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password
# Function to decode an encoded password by shifting each digit down by 3 numbers
def decode_password(encoded_password):
    # Partner does this
    pass

# Menu and user input that calls functions
while True:
    print("\nMenu\n-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")

    if option == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")

    elif option == "2":
        decoded_password = decode_password(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

    elif option == "3":
        break

    else:
        print("Invalid option. Please choose a valid option (1, 2, or 3).")