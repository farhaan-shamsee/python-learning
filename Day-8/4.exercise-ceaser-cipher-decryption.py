"""

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
    amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

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
        decrypted_text += alphabet[(index_of_i-shift_amount)]

    print(f"The encoded text is {decrypted_text}")


if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text_to_encrypt=text, shift_amount=shift)
elif direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text_to_decrypt=text, shift_amount=shift)
else:
    print("Invalid selection")

