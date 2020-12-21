from cryptography.fernet import Fernet

keyFile = 'enc.key'

def getFile():
    myFile = input()
    return myFile

def createKey():
    key = Fernet.generate_key()
    with open (keyFile, 'wb') as encKey:
        encKey.write(key)

def getKey():
    with open(keyFile, 'rb') as encKey:
        key = encKey.read()
    return key

def encryptFile():
    #open original file
    with open(myFile, 'rb') as file:
        original = file.read()
    #create an encrypted file
    with open (encFile, 'wb') as file:
        file.write(Fernet(getKey()).encrypt(original))

print("Enter name of the file you want to encrypt")
myFile = getFile()
encFile = 'encrypted_' + myFile
print("Encrypting... ")
createKey()
encryptFile()
print('Done! The name of encrypted file is "' + encFile +'"')
input()