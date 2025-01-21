def main():
    #Write a program that asks the user to enter a series of single-digit numbers with nothing 
    #separating them. The program should display the sum of all the single digit numbers in the 
    #string. For example, if the user enters 2514, the method should return 12, which is the sum 
    #of 2, 5, 1, and 4. 

    numbers = input("Enter a series of single digit numbers with no space in between: ")  #main string

    sum = 0                               #cache for loopo
    for x in range(len(numbers)):
        sum = sum + int(numbers[x])       #casting each string character into int and adding to cache

    print(f"The sum of the single digit numbers in the string is {sum}.")
        
    
main()
