from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

output_file = "encryptedFile.txt"
input_file = "test.txt"
salt = get_random_bytes(16)

file_in = open(input_file,"r")
file_in = file_in.read().encode()

#creating key from pw and salt by using hash algorithm PBKDF2
def keyDerivingFunction(password,salt):
    return PBKDF2(password,salt,32)
 
#encrypting the file
def encryption(key,data,output_file):
    cipher = AES.new(key,AES.MODE_EAX)
    cipherText,tag = cipher.encrypt_and_digest(data)
    print(cipherText)
    file_out = open(output_file,"wb")
    file_out.write(cipher.nonce)
    file_out.write(tag)
    file_out.write(cipherText)
    file_out.close()

#decrypting the file
def decryption(key,encFile):
    encFile = open(encFile,"rb")
    nonce = encFile.read(16)
    tag = encFile.read(16)
    encData = encFile.read()
    cipher = AES.new(key, AES.MODE_EAX,nonce=nonce)
    plaintext = cipher.decrypt(encData)
    try:
        cipher.verify(tag)
        print("good to go boiz: ", plaintext.decode())
    except ValueError:
        print("incorrect key or corrupted message")



key = keyDerivingFunction("hello",salt)
encryption(key,file_in,output_file)
decryption(key,output_file)




