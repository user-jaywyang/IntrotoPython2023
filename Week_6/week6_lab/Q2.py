def main():
# For this problem, use a dictionary whose keys are month names and whose values are the number of days in the corresponding months. 
# (a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month. 
# (b) Print out all of the keys in alphabetical order. 
# (c) Print out all of the months with 31 days. 
# (d) Print out the (key-value) pairs sorted by the number of days in each month. 

    months = {'January':31 ,'February':29 ,'March':31 ,'April':30 ,'May':31 ,'June':30 ,
             'July':31 ,'August':31 ,'September':30 ,'October':31 ,'November':30 ,'December':31}
    

    print("Part A")
    choice = input("What month are you curious about? \n")
    print(f"There are {months[choice]} days in {choice}.")
    print("\n")
    

    print("Part B")
    for month in sorted(months):   #sorted months by alphabet
        print(month)
    print("\n")


    print("Part C")   
    for month in months:         
        if months[month] == 31:    #check for 31 days
            print(month)
    print("\n")


    print("Part D")
    sorted_dict = {}    #create new dictionary sorted by days
    sorted_values = sorted(months.values())

    for i in sorted_values:       
        for k in months.keys():         #add to new key-values pairs dictionary
            if months[k] == i:          #check for same day values              
                sorted_dict[k] = months[k]   #asign new values

    for x in sorted_dict:                          #output
        print(x + ": " + str(sorted_dict[x])) 
        

if __name__ == '__main__':
    main()
