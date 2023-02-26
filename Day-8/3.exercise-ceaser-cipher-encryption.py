"""

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift
        and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code
    and encrypt a message.

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def encrypt(text_to_encrypt: str, shift_amount: int):
    encrypted_text = ""
    for i in text_to_encrypt:
        index_of_i = alphabet.index(i)
        encrypted_text += alphabet[(index_of_i+shift_amount)]

    print(f"The encoded text is {encrypted_text}")


def decrypt(text_to_decrypt: str, shift_amount: int):
    decrypted_text = ""
    for i in text_to_decrypt:
        index_of_i = alphabet.index(i)
        decrypted_text += alphabet[(index_of_i+shift_amount)]

    print(f"The encoded text is {decrypted_text}")


if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text_to_encrypt=text, shift_amount=shift)
else:
    print("invalid input ")

