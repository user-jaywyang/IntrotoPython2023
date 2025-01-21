import math

def main():
    # Final Project Question 1
    # Author: Jay Yang
    # Date: 12/14/2022
    # Input is survey(s) of people:
    # age (in the range 1 to  120), Residency Status (Local/Foreigner), use of the streaming service regularly (Y/N)

    # Output is the total number of people called, the number  and percentage of who used streaming service regularly
    # The program should also print a table showing the percentages according to residency status and age categories.
    services = []              #list of services
    make_survey(services)            


def make_survey(services):
    #make a new survey
    streaming_name = input("What streaming service will be surveyed? \n")
    streaming_cache = []
    streaming_cache.append(streaming_name)
    streaming_cache.append(add_person())
    cont_add(streaming_cache)                   #send to optional continue to add person
    services.append(streaming_cache)
    cont_survey(services)                       #send to optional add another survey



 
def add_person():
    #add person with (Age, residency, regular status)
    person = [[],[],[]]

    age = int(input("Please enter next person age (1..120): "))                  #check for age
    if age > 120 or age < 1:
        print("ERROR:Please enter integer between 1 and 120")
        return
    else:
        person[0] = age

    residency = input("Please enter this person residency status (L/F): ")                    
    if residency != "F" and residency != "L":                                    #check for residency
        print("ERROR: Please enter integer between 'L' or 'F'.")
        return
    else:
        person[1] = residency

    regular = input("Please enter whether this person use streaming services regularly (Y/N): ")
    if regular != "Y" and regular != "N":                                        #check for regular
        print("ERROR: Please enter integer between 'Y' or 'N'.")
        return
    else:
        person[2] = regular

    return person


def cont_add(streaming_cache):
    #asks to continue adding persons with recursive call
    choice = input("Do you wish to add another person (Y/N)?   ")
    if choice == 'Y':
        streaming_cache.append(add_person())                                     #resend to add person 
        cont_add(streaming_cache)                                                #recursive call 
    elif choice == 'N':
        return
    else:
        print("Please input 'Y' or 'N'")
        cont_add(streaming_cache)


def cont_survey(services):
    #asks to continue adding survey with recursive call

    choice = input("Do you wish to add another survey (Y/N)?   ")
    if choice == 'Y':
        make_survey(services)                                                   #resend to make new survey
    elif choice == 'N':
        print_final(services)                                                   #final print
    else:
        print("Please input 'Y' or 'N'")
        cont_survey(services)

def print_final(services):
    #prints final service report
    for x in services:
        total_persons = len(x)-1
        total_regular = 0
        for y in x[1:] :
            if y[2] == 'Y':
                total_regular += 1

        percent = total_regular/total_persons

        print ("___________________________________________________________________________________ ")
        print(f"Streaming service {x[0]} survey: ")
        print(f"The total number of people called = {total_persons}")
        print(f"The number of people who use the streaming service regularly = {total_regular}  ")
        print(f"The percentage of those who use the streaming service regularly = {percent}")
        
        table(x)                        #separate method for managable size

def table(service):
    #prints final survey table

    #start with making variable for each table input
    total = len(service)-1
    local_under_25 = 0
    local_includeup_25 = 0
    local_total = 0
    foreigner_total = 0
    foreigner_under_25 = 0
    foreigner_includeup_25 = 0

    #loop to count each category of status and age 
    for z in service[1:]:                              
        if z[1]== 'L':
            local_total += 1

            if z[0] < 25:
                local_under_25 += 1
            else:
                local_includeup_25 += 1
        else:
            foreigner_total += 1

            if z[0] < 25:
                foreigner_under_25 += 1
            else:
                foreigner_includeup_25 += 1

    #multiply by 100 to display percent number with no decimal point            
    local_under_25p = (local_under_25/total)*100
    local_includeup_25p = (local_includeup_25/total)*100
    local_totalp = (local_total/total)*100
    foreigner_under_25p = (foreigner_under_25/total)*100
    foreigner_includeup_25p = (foreigner_includeup_25/total)*100
    foreigner_totalp = (foreigner_total/total)*100

    #math.ceil is used to round up 
    print ("________________________________________")
    print ("Residency            Percent under 25              25 and older               Percent Total")
    print (f"Local                     {math.ceil(local_under_25p)}                                {math.ceil(local_includeup_25p)}                                 {math.ceil(local_totalp)}")
    print (f"Foreigner                 {math.ceil(foreigner_under_25p)}                                {math.ceil(foreigner_includeup_25p)}                                  {math.ceil(foreigner_totalp)}")
    print ("________________________________________")
    print (f"Total                 {math.ceil(local_under_25p+foreigner_under_25p)}                               {math.ceil(local_includeup_25p+foreigner_includeup_25p)}                                 {math.ceil(local_totalp+foreigner_totalp)}")
 
    
if __name__ == '__main__':
    main()
