class Patient:
    #contains patient name, address, phone number, and emergency contact info
    def __init__(self, first, middle, last, address, city ,state, zipcode, phone_number, emergency_name, emergency_number):
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone_number = phone_number
        self.__emergency_name = emergency_name
        self.__emergency_number = emergency_number
    
    def set_first(self, first):
        self.__first = first

    def get_first(self):
        return self.__first 
    
    def set_middle(self, middle):
        self.__middle = middle
        
    def get_middle(self):
        return self.__middle
    
    def set_last(self, last):
        self.__last = last
        
    def get_last(self):
        return self.__last
    
    def set_address(self, address):
        self.__address = address
        
    def get_address(self):
        return self.__address
    
    def set_city(self, city):
        self.__city = city
        
    def get_city(self):
        return self.__city
    
    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode

    def get_zipcode(self):
        return self.__zipcode    

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

    def set_emergency_name(self, emergency_name):
        self.__emergency_name = emergency_name

    def get_emergency_name(self):
        return self.__emergency_name 

    def set_emergency_number(self, emergency_number):
        self.__emergency_number = emergency_number

    def get_emergency_number(self):
        return self.__emergency_number  
    
    def __str__(self):
        return 'Personal Information:' + \
               f'Name : {self.__first} {self.__middle} {self.__last} \n' + \
               f'Address : {self.__address}, {self.__city}, {self.__state}, {self.__zipcode} \n' + \
               f'Number : {self.__phone_number} \n' + \
               f'Emergency contact : {self.__emergency_name} \n' + \
               f'Emergency number : {self.__emergency_number} \n' 
