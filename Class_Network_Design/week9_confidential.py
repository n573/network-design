from Cryptodome.Cipher import DES

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

if __name__ == "__main__":
    key = b'abcdefgh'
    des = DES.new(key, DES.MODE_ECB)

    text = 'Hello World!'
    print(text)
    padded_text = pad(text)

    encrypted_text = des.encrypt(bytes(padded_text, 'utf-8'))
    print(encrypted_text)

    print(des.decrypt(encrypted_text))