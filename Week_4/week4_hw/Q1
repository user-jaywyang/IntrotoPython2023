def main():
    #A program that lets the user enter the total rainfall for each of 12 months into a 
    #list. The program should calculate and display the total rainfall for the year, the average 
    #monthly rainfall, the months with the highest and lowest amounts. 
    
    rainlist = list(eval(input("Enter the inches of rainfall each month: ")))              #main list
    MONTHS = 12                                         #magic number for months

    total_rain = 0                                      #cache for loop
    for x in range(len(rainlist)):
        total_rain = total_rain + rainlist[x]
    
    avg = total_rain/MONTHS                             #average
    
    rainlist.sort()                                     #highest and lowest value through index
    high = rainlist[-1]
    low = rainlist[0]
    
    print(f"In total, {total_rain} inches of rainfall fell this year. That is an average of {avg} inches per month.\
    The month with the most rainfall had {high} inches of rain and the least had {low} inches of rain")

    
main()
