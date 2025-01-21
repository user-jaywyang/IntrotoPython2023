class Person():
     #contains personal information name, address, and phone number
    
    #initializer
    def __init__(self, name, address ,number):
        self.__name = name
        self.__address = address
        self.__number = number
    
    #accessor functions
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address 

    def get_number(self):
        return self.__number 
    
    #mutator functions
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

   
    def set_number(self, number):
        self.__number = number
    
    #string
    def __str__(self):
        return f'Name : {self.__name} \n' + \
               f'Address : {self.__address}\n' + \
               f'Number : {self.__number} \n'



class Customer(Person):
    #Subclass of person; adds customer number and yes or no to mailing list

    #initializer
    def __init__(self, name, address, number, cu_number, mailing_list):
        super().__init__(name,address,number) 
        self.__cu_number = cu_number
        self.__mailing_list = mailing_list

    def set_cu_number(self, cu_number):
        self.__cu_number= cu_number

    def get_cu_number(self):
        return self.__cu_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_mailing_list(self):
        return self.__mailing_list
    
    def __str__(self):
        return super().__str__() + \
               f'Customer Number : {self.__cu_number} \n' + \
               f'Mailing List : {self.__mailing_list}\n'
