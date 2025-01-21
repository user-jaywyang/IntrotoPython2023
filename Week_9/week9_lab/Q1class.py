
class Counter():
    #class for counter starting at zero. Can only set counter to 0 and increase or decrease by 1 (NO NEGATIVE NUMBERS)
    
    #initializer
    def __init__(self):
        self.__count = 0
      
    #accessor function
    def get_count(self):
        return self.__count
    
    def display_count(self):
        print(self.__count)

    #mutator function
    def set_count(self, count):
        self.__count = int(count)

    def set_zero(self):
        self.__count = 0
    
    def decrease(self):
        if self.__count > 0:
            self.__count -= 1
        else:
            print('Count is at zero.')

    def increase(self):
        self.__count += 1

    #string
    def __str__(self):
        return f'Count : {self.__count} \n' 
           
    
