class Information:
    #contains personal information name, address, age, and phone number
    
    def __init__(self, name, address, age ,number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number = number
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name 

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address 
    
    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age 
    
    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number 
    
    def __str__(self):
        return f'Name : {self.__name} \n' + \
               f'Address : {self.__address}\n' + \
               f'Age : {self.__age} \n' + \
               f'Number : {self.__number} \n'
