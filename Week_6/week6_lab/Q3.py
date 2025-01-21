def main():
    # A program that uses a dictionary that contains ten user names and passwords. The 
    # program should ask the user to enter their username and password. If the username is not 
    # in the dictionary, the program should indicate that the person is not a valid user of the  
    # system.  If the username is in the dictionary, but the user does not enter the right password, 
    # the program should say that the password is invalid. If the password is correct, then the 
    # program should tell the user that they are now logged in to the system. 

    database = {"Indiana":"Jones", "Han":"Solo", "Snake":"Plisken", "John":"Rambo", "Rick":"Deckard", 
               "Marty":"McFly", "Karate":"Kid", "Cobra":"Kai", "Bruce":"Lee", "Captain":"Underpants"}
    
    ask(database)
    

def ask(database):
    #main function of program, seperated from sample user/password dictionary 

    username = input("Hello! Please enter username: ")

    if username in database:                           #check username
        password = input("Please enter password: ")

        if password == database[username]:             #check password
            print("Logged into system. Good hunting cowboy!")                       #exit
        else:
            print("Wrong password!")
            ask(database)                              #recursive to continue query
    else:
        print("No such username exists :(")
        ask(database)                                  #recursive to continue query
        
if __name__ == '__main__':
    main()
