class RetailItem:
    #contains item description, units in inventory, price
    
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price
       
    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description 

    def set_units(self, units):
        self.__units = units

    def get_units(self):
        return self.__units
    
    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price 
    
  
    def __str__(self):
        return f'Description : {self.__description} \n' + \
               f'Units in inventory : {self.__units}\n' + \
               f'Price : {self.__price} \n' 
