import random

class Encript:
    
    data = ''
    
    def __init__(self):
        with open(r'The_Encript/words.txt', 'r') as file:
            self.data = file.read()

    def generate_key(self):
        # Generate a key for the encryption
        print('Generating a key for the encryption...')
        key = random.randbytes(32)
        return key
    
    def encrypt(self, key):
        # Encrypt the text
        print('Encrypting the text...')
        encrypted_text = ''
        for i in range(len(self.data)):
            encrypted_text = 
            #encrypted_text =
        return encrypted_text
     
    def save_key(self):
        # Save the key to a file
        print('Saving the key...')
        
    def save_encrypted_text(self):
        # Save the encrypted text to a file
        print('Saving the encrypted text...')
        with open(r'The_Encript/encrypted_text.txt', 'w') as file:
            file.write(self.encrypt())
    

class Decript:
    
    def __init__(self):
        with open(r'The_Encript/words.txt', 'r') as file: 
            self.data = file.read()

    def get_key(self):
        if input('Do you have a key? (y/n)') == 'y':
            self.input_key = input('Enter the key: ')
        else:
            print('You need a key to decrypt the text.')
    def decrypt(self, text):
        print('Decrypting the text...')

    def save_decrypted_text(self):
        with open(r'The_Encript/decrypted_text.txt', 'w') as file:
            file.write(self.decrypt())

temp_key = (Encript.generate_key(self=Encript))
print(temp_key)
temp_encrypted_text = Encript.encrypt(self=Encript, key=temp_key)
print(temp_encrypted_text)
