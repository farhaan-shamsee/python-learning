# """
# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# """
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def caesar(start_text: str, shift_amount: int, enc_or_dec: str):
    final_text = ""
    for i in start_text:
        index_of_i = alphabet.index(i)
        # my code below:
        # if enc_or_dec == 'encode':
        #     final_text += alphabet[(index_of_i+shift_amount)]
        # elif enc_or_dec == 'decode':
        #     final_text += alphabet[(index_of_i - shift_amount)]
        # more efficient code below:
        if enc_or_dec == 'decode':
            shift_amount *= -1
        final_text += alphabet[(index_of_i + shift_amount)]
    print(f"The {enc_or_dec}d text is {final_text}")


if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, enc_or_dec=direction)
elif direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, enc_or_dec=direction)
else:
    print("Invalid selection")
