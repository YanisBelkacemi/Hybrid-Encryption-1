from cryptidy import symmetric_encryption, asymmetric_encryption
import os
import shutil
distination_key ='C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid Encryption\\key'
sym_key = symmetric_encryption.generate_key()
asy_key = asymmetric_encryption()
path = 'C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid Encryption\\testingfiles'
files = []

for file in os.listdir(path):
    files.append(file)


with open('key.bin' , 'wb') as keyenc:
    keyenc.write(sym_key)
for f in files :
    fullpath = os.path.join(path, f)
    with open(fullpath , 'rb') as mylovedfile:
        mlf = mylovedfile.read()

    enc = symmetric_encryption.encrypt_message(mlf, sym_key)
    with open(fullpath , 'wb') as mylovedfuckedfile:
        mylovedfuckedfile.write(enc)

shutil.copy('C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid Encryption\\key.bin' , distination_key)
