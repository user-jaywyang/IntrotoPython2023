class Procedure: 
    #contains procedure name, date, practioner who performed procedure, charge for procedure 
    
    def __init__(self, name, date, practitioner, charge):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
       
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date
    
    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def get_practitioner(self):
        return self.__practitioner
    
    def set_charge(self, charge):
        self.__charge = charge

    def get_charge(self):
        return self.__charge
    
    def __str__(self):
        return f'Procedure name : {self.__name} \n' + \
               f'Date : {self.__date}\n' + \
               f'Performed by : {self.__practitioner}\n' + \
               f'Charge : {self.__charge} \n' 
