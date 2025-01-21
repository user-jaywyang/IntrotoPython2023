def main():
    #Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. 
    #It should print the date in the format March 12, 2018. 
    
    date = input("Enter a date in the format 'mm/dd/yyyy': ")
    date_list = list(date)                                   #cast string into list
    
    for x in range(len(date_list) - 2):                      #for loop range is -2 because of two slashes that will be removed
        if date_list[x] == "/":
            del date_list[x]
    
    month = int(date_list[0] + date_list[1])                 #combine list indexes to create date strings and cast them to ints
    day = int(date_list[2] + date_list[3])
    year = int(date_list[4] + date_list[5] + date_list[6] + date_list[7])

    if month == 1:                                           #conditionals for changing month date to name
        month = "January"

    elif month == 2:
        month = "February"

    elif month == 3:
        month = "March"

    elif month == 4:
        month = "April"

    elif month == 5:
        month = "May"

    elif month == 6:
        month = "June"

    elif month == 7:
        month = "July"

    elif month == 8:
        month = "August"

    elif month == 9:
        month = "September"

    elif month == 10:
        month = "October"

    elif month == 11:
        month = "November"

    elif month == 12:
        month = "December"

    print(f"The date is {month} {day}, {year}.")
        
main()
