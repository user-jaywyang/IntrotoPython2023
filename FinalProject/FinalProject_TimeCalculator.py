def main():
    # Final Project Question 2
    # Author: Jay Yang
    # Date: 12/14/2023
    # Input is two different times in (hh:mm am/pm)
    # Output is the difference of MINUTES between two input times

    print("TIME DIFFERENCE")
    first = input("Enter first time (hh:mm am/pm): ")
    second = input("Enter second time (hh:mm am/pm): ")
    menu(first, second)

def menu(first, second): 
    #menu handles two times and finds difference; adds call to cont to ask user
    first_min = transform(first)
    second_min = transform(second)
    difference = abs(first_min - second_min)                   #absolute value of difference
    print(f"The difference is {difference} minute(s)")
    cont()

def transform(x):
    #inputs a time and converts to total minutes
    index = x.index(':')        #index of colon notation helps "0 in front of integer" input of hour
    hour =  int(x[:index])
    hour_min = hour * 60
    min = int(x[index+1:index+3]) #index requires two digits
    total = hour_min + min
    if "pm" in x:                 #have AM start as base and convert all PM hours to military time
        total += 720
    return total

def cont():
    #asks to continue another time comparison to user w/ recursive call
    choice = input("Do you wish to continue (Y/N)?   ")
    if choice == 'Y':
        main()
    elif choice == 'N':
        return
    else:
        print("Please input 'Y' or 'N'")
        cont()
  
if __name__ == '__main__':
    main()
