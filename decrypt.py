from cryptography.fernet import Fernet

keyFile = 'enc.key'

def getFile():
    myFile = input()
    return myFile

def getKey():
    with open(keyFile, 'rb') as encKey:
        key = encKey.read()
    return key

def decryptFile():
    #open encrypted file
    with open(encFile, 'rb') as file:
        original = file.read()
    #decrypt an encrypted file
    with open (newFile, 'wb') as file:
        file.write(Fernet(getKey()).decrypt(original))

print("Make sure that the key file's name is" + '"enc.key"')
print("Enter name of the file you want to decrypt")
encFile = input()
newFile = 'dencrypted_' + encFile
print("Decrypting... ")
decryptFile()
print('Done! The name of the decrypted file is "' + newFile +'"')
input()