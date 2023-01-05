print('Welcome to the..')
print('''
╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ╦  ╦┌─┐┬  ┬┌┬┐┌─┐┌┬┐┌─┐┬─┐┬
╠═╝├─┤└─┐└─┐││││ │├┬┘ ││  ╚╗╔╝├─┤│  │ ││├─┤ │ │ │├┬┘│
╩  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘   ╚╝ ┴ ┴┴─┘┴─┴┘┴ ┴ ┴ └─┘┴└─o
''')


def validate_pwd(password):
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    val = True

    if len(password) < 16:
        print('Password must consist 16 characters long. Please try again.')
        val = False

    if len(password) > 25:
        print('You have exceed the maximum amount of 25 characters. Please try again.')
        val = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one number. Please try again.')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter. Please try again.')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter. Please try again.')
        val = False

    if not any(char in symbols for char in password):
        print('Password should have at least one special character such as !, $, &, etc. Please try again.')
        val = False
    if val:
        return val


# Main method
def main():
    password = 'Y00feeC0de$!'

    if validate_pwd(password):
        print("Password is valid")
    else:
        print("Invalid Password !!")


# Driver Code
if __name__ == '__main__':
    main()
