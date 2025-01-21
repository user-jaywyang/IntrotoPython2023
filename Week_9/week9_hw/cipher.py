import caesar, railfence

def main():
    #function to control use of either CAESAR or RAILFENCE methods for encryption or decyryption
    print("Hello! Welcome to the cypher program!")
    mode = input("Which cypher would you like to use? \n 1. Caesar \n 2. Railfence \n: ")
    mode = mode.upper()                            #UPPERCASE
    if mode == "CAESAR":                           #Check cypher choice
        caesar_mode()
    elif mode == "RAILFENCE":
        railfence_mode()
    else:
        print('Please enter either Caesar or Railfence')


def caesar_mode():
    #function to CAESAR encryption or decyryption
    choice = input('Would you like to encrypt or decyrypt? \n : ')             #Check encryption direction choice
    choice = choice.upper()
    if choice == "ENCRYPT":
        plain = input("Please enter a text to encrypt: ")
        text = caesar.Caesar(plain)
        key = int(input('Please enter a key integer: '))
        print(f'The encrypted text is: {text.encrypt(key)}')

    elif choice == "DECYRYPT":
        text = caesar.Caesar('')
        plain = input("Please enter a cypher-text to decyrypt: ")
        key = int(input('Please enter a key integer: '))
        print(f'The decyrypted text is: {text.decyrypt(plain, key)}')
    
    else:
        print('Please enter either Encrypt or Decyrypt')


        
def railfence_mode():
    #function to RAILFENCE encryption or decyryption
    choice = input('Would you like to encrypt or decyrypt? \n : ')              #Check encryption direction choice
    choice = choice.upper()
    if choice == "ENCRYPT":
        plain = input("Please enter a text to encrypt: ")
        text = railfence.Railfence(plain)
        key = input(int('Please enter a key integer: '))
        print(f'The encrypted text is: {text.encrypt(key)}')

    elif choice == "DECYRYPT":
        text = railfence.Railfence('')
        plain = input("Please enter a cypher-text to decyrypt: ")
        key = input(int('Please enter a key integer: '))
        print(f'The decyrypted text is: {text.decyrypt(plain, key)}')
    
    else:
        print('Please enter either Encrypt or Decyrypt')

if __name__ == '__main__':
    main()
