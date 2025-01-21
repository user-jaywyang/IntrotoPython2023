def main():
    # Design a function that accepts an integer argument and returns the sum of 
    # all the integers from 1 up to the number passed as an argument. For example, 
    # if 50 is passed as an argument, the function will return the sum of 1, 2, 3, 4, . . . 
    # 50. Use recursion to calculate the sum. 
    x = int(input("Enter an integer: "))
    sum = add(x)
    print(f"The integer squished together is {sum}!")

def add(x):
    #function adds all integers from 1 to accepted int argument

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + add(x-1)       #LOOP WITH SUM OF SHRINKING X VALUE

if __name__ == '__main__':
    main()
