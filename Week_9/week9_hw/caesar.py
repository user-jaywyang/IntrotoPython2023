import string

class Caesar():
    #Class for encrypting and decyrypting with CAESAR cypher
    
    #intializer
    def __init__(self, plain):
        self.__plain = plain
         

    #mutator and accessor    
    def set_plain(self, plain):
        self.__plain = plain

    def get_plain(self):
        return self.__plain

    def encrypt(self, key):
        new_plain = transform(self.__plain)       #remove spaces and punctuation
        new_plain = key_switch(new_plain, key)
        return new_plain

    def decyrypt(self, cypher_text, key):
        decyphered = deswitch(cypher_text, key)
        return decyphered

    
    def __str__(self):
        return f'Original text : {self.__plain}'

def transform(plain):
    #changes text to one without spaces or punctuation
        plain = plain.upper()
        new_plain = ''             #new string
        for x in plain:
            if x in string.punctuation:      #skip/remove conditionals
                pass
            elif x == ' ':
                pass
            elif x.isdigit():    
                pass
            else:
                new_plain += x 
        return new_plain

def key_switch(plain, key):
    #main engine of encryption function
    cache = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    new_plain = ''
    for x in plain:
        new_index = cache.index(x) + key
        if new_index > 25:                        #check for key index out of range
            new_index = new_index - 26
        elif key < 0:                             #check for key index out of range
            new_index = 26 + new_index
        new_plain += cache[new_index]
    return new_plain

def deswitch(cypher_text, key):
    #main engine of decyryption function
    cache = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    cypher_text = cypher_text.upper()
    decryption = ''
    for x in cypher_text:                             
        new_index = cache.index(x) - key
        if new_index > 25:                       #check for key index out of range
            new_index = new_index + 26
        elif key < 0:                            #check for key index out of range
            new_index = 26 - new_index
        decryption += cache[new_index]
    return decryption




