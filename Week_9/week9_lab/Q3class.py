class Rational():
    #represents rational number with numerator an denominator as attributes

    #initializer
    def __init__(self, numerator, denominator):        
        self.__numerator = int(numerator)
        self.__denominator= int(denominator)
      
    #accessor function
    def get_numerator(self):
        return self.__numerator
    
    def get_denominator(self):
        return self.__denominator
    
    def display_value(self):
        num = self.__numerator/self.__denominator
        print(f"Rational number value is:{num}")

    #mutator function
    def set_numerator(self, new):
        self.__numerator = new
    
    def set_denominator(self, new):
        if new > 0:
            self.__denominator = new
        else:
            print("ERROR: Denominators must be greater than 0")
    

    #string
    def __str__(self):
        return f'Numerator : {self.__numerator} \n' +\
            f'Denominator : {self.__denominator} \n'
         
