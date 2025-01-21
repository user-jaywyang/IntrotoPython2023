import random 

def main():
    # Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as 
    # values. (Use the Internet to get a list of the states and their capitals.) The program should then 
    # randomly quiz the user by displaying the name of a state and asking the user to enter that state’s 
    # capital. The program should keep a count of the number of correct and incorrect responses. (As an 
    # alternative to the U.S. states, the program can use the names of countries and their capitals.) 
    
    states_capitals = dictionary()
    print("Welcome to the great State Capital quiz!")
    quiz(states_capitals)

def quiz(states_capitals):
    #main quiz function
    
    state_list = list(states_capitals.keys())        #list of states
    random.shuffle(state_list)                       #shuffle out of alphabetical order
    count = 0                                        #points count

    for state in state_list:                                     
        choice = input(f"What is the capital of {state}? : ")
        if choice == states_capitals[state]:
            count += 1
            print("Correcto!")
        else:
            print("Wrong!")   
    print(f"Alright! You got {count} state capitals correct!")

def dictionary(): 
    #constructs dictionary of states and capitals

    states_capitals =  {'Alabama': 'Montgomery',
                        'Alaska': 'Juneau',
                        'Arizona':'Phoenix',
                        'Arkansas':'Little Rock',
                        'California': 'Sacramento',
                        'Colorado':'Denver',
                        'Connecticut':'Hartford',
                        'Delaware':'Dover',
                        'Florida': 'Tallahassee',
                        'Georgia': 'Atlanta',
                        'Hawaii': 'Honolulu',
                        'Idaho': 'Boise',
                        'Illinios': 'Springfield',
                        'Indiana': 'Indianapolis',
                        'Iowa': 'Des Moines',
                        'Kansas': 'Topeka',
                        'Kentucky': 'Frankfort',
                        'Louisiana': 'Baton Rouge',
                        'Maine': 'Augusta',
                        'Maryland': 'Annapolis',
                        'Massachusetts': 'Boston',
                        'Michigan': 'Lansing',
                        'Minnesota': 'St. Paul',
                        'Mississippi': 'Jackson',
                        'Missouri': 'Jefferson City',
                        'Montana': 'Helena',
                        'Nebraska': 'Lincoln',
                        'Neveda': 'Carson City',
                        'New Hampshire': 'Concord',
                        'New Jersey': 'Trenton',
                        'New Mexico': 'Santa Fe',
                        'New York': 'Albany',
                        'North Carolina': 'Raleigh',
                        'North Dakota': 'Bismarck',
                        'Ohio': 'Columbus',
                        'Oklahoma': 'Oklahoma City',
                        'Oregon': 'Salem',
                        'Pennsylvania': 'Harrisburg',
                        'Rhoda Island': 'Providence',
                        'South Carolina': 'Columbia',
                        'South Dakota': 'Pierre',
                        'Tennessee': 'Nashville',
                        'Texas': 'Austin',
                        'Utah': 'Salt Lake City',
                        'Vermont': 'Montpelier',
                        'Virginia': 'Richmond',
                        'Washington': 'Olympia',
                        'West Virginia': 'Charleston',
                        'Wisconsin': 'Madison',
                        'Wyoming': 'Cheyenne'}

    return states_capitals
 


if __name__ == '__main__':
    main()
