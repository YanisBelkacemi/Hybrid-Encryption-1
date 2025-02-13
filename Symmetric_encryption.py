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
    with open(fullpath , 'rb') as Target:
        Encryption_target_variable = Target.read()

    Encryption_function = symmetric_encryption.encrypt_message(Encryption_target_variable, sym_key)
    with open(fullpath , 'wb') as Final_step:
        Final_step.write(Encryption_function)

shutil.copy('C:\\Users\\ASUS\\Documents\\cookbook\\Hybrid Encryption\\key.bin' , distination_key)
# here starts the 2nd encryption 

private_Key,public_key = asymmetric_encryption.generate_keys()

with open('private_key.bin', 'wb') as private_Key_file:
    private_Key.write(private_Key_file)

with open('key.bin', 'rb') as key :
    symmetric_key = key.read()

asymmetric_encryption_funtion = asymmetric_encryption.encrypt_message(symmetric_key , public_key)

with open('key.bin' , 'wb') as Final_step_asymmetric:
    Final_step_asymmetric.write(asymmetric_encryption_funtion)
