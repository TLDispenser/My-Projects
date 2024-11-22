import secrets
import random
https://stackoverflow.com/questions/35630242/encrypting-a-message-using-secret-key-in-python
class Encript:
    
    def __init__(self):
        with open(r'The_Encript/words.txt', 'r') as file:
            self.data = file.read()
            

    def generate_key(self):
        # Generate a key for the encryption
        print('Generating a key for the encryption...')
        key = Generate_Passowrd.generate_password(Generate_Passowrd)
        return key
    
    def encrypt(self, key):
        # Encrypt the text
        character_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?'
        print('Encrypting the text...')
        table = {x: y for (x, y) in zip(character_set,key )}
        return "".join( map(lambda x:table.get(x,x),self.data) )
        
     
    def save_key(self):
        # Save the key to a file
        print('Saving the key...')
        
    def save_encrypted_text(self):
        # Save the encrypted text to a file
        print('Saving the encrypted text...')
        with open(r'The_Encript/encrypted_text.txt', 'w') as file:
            file.write(self.encrypt())
    

class Decript:
    data = ''
    def __init__(self):
        with open(r'The_Encript/words.txt', 'r') as file: 
            self.data = file.read()
            
    def get_key(self):
        if input('Do you have a key? (y/n)') == 'y':
            self.input_key = input('Enter the key: ')
        else:
            print('You need a key to decrypt the text.')
    def decrypt(self, input_key):
        character_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?'
        print('Decrypting the text...')
        temporary_input = input("Enter the jumb;le: ")
        temp_key = input("Enter the key: ")
        table = {x: y for (x, y) in zip(character_set,temp_key )}
        return "".join( map(lambda x:table.get(x,x),temporary_input) )
        #return "".join( map(lambda x:table.get(x,x),self.data) )
    def save_decrypted_text(self):
        with open(r'The_Encript/decrypted_text.txt', 'w') as file:
            file.write(self.decrypt())



class Generate_Passowrd:
    def generate_password(self):
        print('Generating a password...')
        random_one = random.randint(0, 2)
        if random_one == 0:
            password = secrets.token_hex(128)
        elif random_one == 1:
            password = secrets.token_bytes(128)
        elif random_one == 2:  
            password = secrets.token_urlsafe(128)
        return password



temp_data = Encript()
temp_key = temp_data.generate_key()
print(temp_key)
print(temp_data.encrypt(temp_key))

temp_return = Decript()
keyy = temp_return.get_key()
print(temp_return.decrypt(keyy))
#for i in range(10):
#    print(Generate_Passowrd.generate_password(Generate_Passowrd))
