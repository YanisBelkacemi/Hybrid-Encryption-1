from cryptidy import symmetric_encryption, asymmetric_encryption
import os
import shutil

class FileEncryptor:
    def __init__(self, path):
        self.path = path
        self.files = os.listdir(path)
        self.sym_key = symmetric_encryption.generate_key()

    def encrypt_files(self):
        for f in self.files:
            fullpath = os.path.join(self.path, f)
            with open(fullpath, 'rb') as target:
                encryption_target_variable = target.read()

            encryption_function = symmetric_encryption.encrypt_message(encryption_target_variable, self.sym_key)
            with open(fullpath, 'wb') as final_step:
                final_step.write(encryption_function)

class KeyManager:
    def __init__(self, key_path):
        self.key_path = key_path

    def save_symmetric_key(self, sym_key):
        with open('key.bin', 'wb') as key_file:
            key_file.write(sym_key)

    def copy_key(self):
        shutil.copy('key.bin', self.key_path)

class AsymmetricEncryptor:
    def __init__(self):
        self.private_key, self.public_key = asymmetric_encryption.generate_keys()

    def save_private_key(self):
        with open('private_key.bin', 'wb') as private_key_file:
            private_key_file.write(self.private_key)

    def encrypt_symmetric_key(self):
        with open('key.bin', 'rb') as key_file:
            symmetric_key = key_file.read()
        
        encrypted_symmetric_key = asymmetric_encryption.encrypt_message(symmetric_key, self.public_key)
        
        with open('key.bin', 'wb') as final_step_asymmetric:
            final_step_asymmetric.write(encrypted_symmetric_key)

# Main execution
if __name__ == "__main__":
    # Define paths
    destination_key = 'C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid-Encryption-1\\key'
    path = 'C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid-Encryption-1\\testingfiles'

    # Encrypt files
    file_encryptor = FileEncryptor(path)
    file_encryptor.encrypt_files()

    # Manage keys
    key_manager = KeyManager(destination_key)
    key_manager.save_symmetric_key(file_encryptor.sym_key)
    key_manager.copy_key()

    # Asymmetric encryption
    asymmetric_encryptor = AsymmetricEncryptor()
    asymmetric_encryptor.save_private_key()
    asymmetric_encryptor.encrypt_symmetric_key()
