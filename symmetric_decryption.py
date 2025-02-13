from cryptidy import symmetric_encryption , asymmetric_encryption
import os

def AsymmetricDecryption():

    with open('private_key.txt' , 'r') as private_key :
         

         key = private_key.read()
    with open('key.bin' , 'rb') as sym_key:
        coded_key = sym_key.read()
    _,asymmetric_decryption = asymmetric_encryption.decrypt_message(coded_key , key)
    # decode('utf') is used here to decode the decrypted data
    with open('key.bin' , "wb") as Unlocked_key:
        Unlocked_key.write(asymmetric_decryption)




def SymmetricDecryption():
    path = 'C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid-Encryption-1\\testingfiles'
    files = []
    # sym part
    for file in os.listdir(path):
        files.append(file)
    with open('key.bin' , 'rb') as key:
        readkey = key.read()
    for f in files :
        fullpath = os.path.join(path, f)
        with open(fullpath , 'rb') as Target:
            Target_variable = Target.read()
        _, decryption = symmetric_encryption.decrypt_message(Target_variable, readkey)
        with open(fullpath , 'w') as Unlocked_file:
                Unlocked_file.write(decryption.decode('utf-8'))


