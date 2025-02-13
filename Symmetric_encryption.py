from cryptidy import symmetric_encryption, asymmetric_encryption
import os
import shutil

class SymmetricEncryption():
    def __init__(self , path):
        self.path = path
        self.files = os.listdir(path)
        self.sym_key = symmetric_encryption.generate_key()
    def encrypt_files(self):
        for f in self.files :
            fullpath = os.path.join(path, f)
            with open(fullpath , 'rb') as Target:
                Encryption_target_variable = Target.read()

            Encryption_function = symmetric_encryption.encrypt_message(Encryption_target_variable, self.sym_key)
            with open(fullpath , 'wb') as Final_step:
                Final_step.write(Encryption_function)
class KeyManager():
    def __init__(self , key_path):
        self.key_path = key_path
    def symmetric_key(self , symmetric_key):
        with open('key.bin' , 'wb') as keyenc:
            keyenc.write(symmetric_key)

class AsymmetricEncryption():
    def __init__(self):
        self.private_key , self.public_key = asymmetric_encryption.generate_keys()
    def asymmetric_key(self):
        with open('private_key.txt', 'w') as private_Key_file:
            private_Key_file.write(self.private_key)
    def encrypt_symmetric_key(self) :
        with open('key.bin', 'rb') as key :
            symmetric_key = key.read()

        asymmetric_encryption_funtion = asymmetric_encryption.encrypt_message(symmetric_key , self.public_key)

        with open('key.bin' , 'wb') as Final_step_asymmetric:
            Final_step_asymmetric.write(asymmetric_encryption_funtion)



if __name__ == '__main__':
    distination_key ='C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid-Encryption-1\\key'
    path = 'C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid-Encryption-1\\testingfiles'
# File Encryption
    Encryption_Files = SymmetricEncryption(path)
    Encryption_Files.encrypt_files()
# Saving the SymmetricKey
    Save_Key = KeyManager(distination_key)
    Save_Key.symmetric_key(Encryption_Files.sym_key)

# Encrypting key
    Key_Encryptor = AsymmetricEncryption()
    Key_Encryptor.asymmetric_key()
    Key_Encryptor.encrypt_symmetric_key()
