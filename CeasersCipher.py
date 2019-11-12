plain_txt = input("Enter plain text here: ")
cipher_txt = input("Enter cipher text here: ")
shift = int(input("Enter shift no.: "))


def encryption(plaintext, key):
    cipher = []
    cipher_text = [ord(x) for x in plaintext if ord(x) is not 32]
    for x in cipher_text:
        if x < 65 or x > 122 or 90 > x > 97:
            cipher.append(chr(x))
        elif 91 > x > 64:
            x = x + key
            if x > 90:
                x = (x - 90) + 64
            cipher.append(chr(x))
        elif 123 > x > 96:
            x = x + key
            if x > 122:
                x = (x - 122) + 96
            cipher.append(chr(x))
    cipher = ''.join(map(str,cipher))
    return cipher


def decryption(cipher_text, key):
    text = []
    plaintext = [ord(x) for x in cipher_text]
    for x in plaintext:
        if x < 65 or x > 122 or 90 > x > 97:
            text.append(chr(x))
        elif 64 < x < 91:
            x = x - key
            if x < 65:
                x = x + 26
            text.append(chr(x))
        elif 96 < x < 123:
            x = x - key
            if x < 97:
                x = x + 26
            text.append(chr(x))
    text = ''.join(map(str, text))
    return text


print(encryption(plain_txt, shift))
print(decryption(cipher_txt, shift))