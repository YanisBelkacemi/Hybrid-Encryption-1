from cryptidy import symmetric_encryption, asymmetric_encryption
import os
import shutil

distination_key ='C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid-Encryption-1\\key'
sym_key = symmetric_encryption.generate_key()

path = 'C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid-Encryption-1\\testingfiles'
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
# here starts the 2nd encryption 

private_Key,public_key = asymmetric_encryption.generate_keys()