from cryptidy import symmetric_encryption
import os

path = 'C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid Encryption\\testingfiles'
files = []

for file in os.listdir(path):
    files.append(file)

with open('key.bin' , 'rb') as key:
    readkey = key.read()

for f in files :
    fullpath = os.path.join(path, f)
    with open(fullpath , 'rb') as mylovedfile:
        mlf = mylovedfile.read()

    _, dyc = symmetric_encryption.decrypt_message(mlf, readkey)
    with open(fullpath , 'w') as mylovedfuckedfile:
            mylovedfuckedfile.write(dyc.decode('utf-8'))
