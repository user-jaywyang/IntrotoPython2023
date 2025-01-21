def main():
    #Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers in a list then display the following data: 
    #• The lowest number in the list 
    #• The highest number in the list 
    #• The total of the numbers in the list 
    #• The average of the numbers in the list
    intlist = list(eval(input("Enter twenty numbers: ")))          #main list
    length = len(intlist)

    intlist.sort()                       #get highest and lowest values through sorted indexes
    low = intlist[0]
    high = intlist[-1]
    
    total_sum = 0                        #cache for loop sum
    for x in range(length):
        total_sum = total_sum + intlist[x]

    avg = total_sum/length               #average

    print(f"The lowest number in the list is {low} and the highest number in the list is {high}.\
 The sum of the number is {total_sum} and the average is {avg}")
    
main()
