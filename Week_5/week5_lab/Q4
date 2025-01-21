import random

def main():
    num = eval(input("Enter an integer: "))
    function(num)

def function(num):
    #Function that takes an integer n and returns a random integer with exactly 
    #n  digits. For instance, if n is 3, then 125 and 593 would be valid return values, 
    #but 093 would not because that is really 93, which is a two-digit number. 

    new_num = ""                              #initialize new string a.k.a cache for loop

    for x in range(num):             
        s = str(random.randint(1, 9))         #cast random int into string
        new_num = new_num + s                 #add int character to cache string

    new_num = int(new_num)                    #cast back into int value
    print(new_num)

main()
