#!/usr/bin/python

def checkHex(s):
    try:
        int(s,16)
        return True
    except ValueError:
        return False



def xor_cipher_hex(text, key):
    result = ''
    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return result.encode('utf-8').hex()


def xor_cipher_hex_decode(message, key):
    enc_message = '0x'+message
    final_enc_message = enc_message[2:]
    bytes_obj = bytes.fromhex(final_enc_message)
    ascii_sting = bytes_obj.decode('ASCII')
    result = ""
    for i in range(len(ascii_sting)):
        result += chr(ord(ascii_sting[i]) ^ ord(key[i % len(key)]))
    return result

def main():
    print("""\033[1;36m1. Encrypt\033[0m
\033[1;36m2. Decrypt\033[0m
\033[1;36m3. Exit\033[0m
    """)
    enc_dec = input("[*] Enter the number: ")

    if enc_dec == "1":

        message = input("\033[1;30m[*] Enter your message: \033[0m")

        while not message:
            print("[-] Message cannot be encrypted if it's empty!!")
            message = input("\033[1;30m[*] Enter your message: \033[0m")

        key = input("\033[1;30m[*] Enter the key to encrypt: \033[0m")
        while not key:
            print("[-] Key is necessary to lock.")
            key = input("\033[1;30m[*] Enter the key to encrypt: \033[0m")

        print(f'''
[+] The encrypted message is: \033[1;32m {xor_cipher_hex(message,key)}\033[0m
                                                                           ''')



    elif enc_dec == "2":

        message = input("\033[1;30m[*] Enter the encrypted message: \033[0m")
        while checkHex(message) == False:
            print("[-] Message cannot be decrypted if it's empty and must be in hexadecimal format!!")
            message = input("\033[1;30m[*] Enter the encrypted message: \033[0m")

        key = input("\033[1;30m[*] Enter the key to decrypt: \033[0m")
        while not key:
            print("[-] Key is necessary to unlock.")
            key = input("\033[1;30m[*] Enter the key to decrypt: \033[0m")

        print(f'Message is {message}')

        print(f'''
[+] The decrypted message is:  \033[1;35m{xor_cipher_hex_decode(message, key)}\033[0m                                                                                ''')

    elif enc_dec == "3":
        exit()

    else:
        print("[-] You enetered something else.")
        print("")

while True:
    main()
