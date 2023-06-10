from cryptography.fernet import Fernet
key = Fernet.generate_key()
 
# string the key in a file
with open('key_file.key', 'wb') as key_file:
   key_file.write(key)
with open('key_file.key', 'rb') as key_file:
    key = key_file.read()
 

fernet = Fernet(key)
with open('test.txt', 'rb') as file:
    original = file.read()
     
###Encryption
encrypted = fernet.encrypt(original)

with open('test.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

 

###Decryption
fernet = Fernet(key)
with open('test.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 

decrypted = fernet.decrypt(encrypted)
 

with open('test.txt', 'wb') as dec_file:
    dec_file.write(decrypted)