class Student():
    # Final Project Question 3 Class
    # Author: Jay Yang
    # Date: 12/14/2022
    # Student contains First name, Last name, ID # (integer), Date of birth (MM/DD/YYYY), Assignment 1 (0-100), Assignment 2 (0-100), Lab (0-10), Final exam (0-100)
    # Two attributes (mark and grade) are only set after intialization with seperate methods 
    
    #intializer
    def __init__(self, first, last, id, dob, a1, a2, lab, final):

        self.__first = str(first)

        self.__last = str(last)

        self.__id = int(id)

        self.__dob = str(dob)
        
        self.__a1 = int(a1)

        self.__a2 = int(a2)

        self.__lab = int(lab)

        self.__final = int(final)
        
        self.__mark = 0                 #will be calculated in method below
        self.__grade = ""               #will be assigned in method below
 
        
    #mutators  
    def set_first(self, first):
        self.__first = first

    def set_last(self, last):
        self.__last = last

    def set_id(self, id):
        self.__id = int(id)

    def set_dob(self, dob):
        self.__dob = dob

    def set_a1(self, a1):
        self.__a1 = int(a1)

    def set_a2(self, a2):
        self.__a2 = int(a2)

    def set_lab(self, lab):
        self.__lab = int(lab)

    def set_final(self, final):
        self.__final = int(final)    


    #accessors
    def get_first(self):
        return self.__first 

    def get_last(self):
        return self.__last 

    def get_id(self):
        return self.__id

    def get_dob(self):
        return self.__dob 

    def get_a1(self):
        return self.__a1 

    def get_a2(self):
        return self.__a2 

    def get_lab(self):
        return self.__lab

    def get_final(self):
        return self.__final   

    def get_mark(self):
        return self.__mark

    
    def compute_mark(self):
        #computes final mark based on 20% weight on both Assignments, 10% weight for Lab, and 50% weight for Final
        mark = 0
        mark += (self.__a1 * 0.2)
        mark += (self.__a2 * 0.2)
        mark += self.__lab 
        mark += (self.__final * 0.5)
        self.__mark = mark
    

    def compute_grade(self):
        #computes final grade based on mark percentile
        if self.__mark > 80:
            self.__grade = "HD"

        elif self.__mark > 70:
            self.__grade =  "D"

        elif self.__mark > 60:
            self.__grade =  "C"

        elif self.__mark > 50:
            self.__grade =  "P"

        else:
            self.__grade =  "N"


    def equals(self, other):
        #compares two instances of Student and returns true if same instance
        if self.__first == other.get_first():
            if self.__last == other.get_last():
                if self.__dob == other.get_dob():
                    if self.__id == other.get_id():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


    def __str__(self):
        #string return
        return f'First name : {self.__first} \n'+ \
               f'Last name : {self.__last} \n' + \
               f'ID : {self.__id} \n' + \
               f'Date of Birth : {self.__dob} \n'+ \
               f'Assignment 1 : {self.__a1} \n' + \
               f'Assignment 2 : {self.__a2} \n' + \
               f'Weekly Lab : {self.__lab} \n'+ \
               f'Final Exam : {self.__final} \n' + \
               f'Final Mark : {self.__mark} \n' + \
               f'Final Grade : {self.__grade} \n'
