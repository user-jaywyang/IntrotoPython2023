def main():
    # Design a recursive function that accepts two arguments into the parameters 
    # x and y. The function should return the value of x times y.  
    # Remember, multiplication can be performed as repeated addition as follows: 
    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))
    value = recursive(x,y)
    print(f"The product of {x} and {y} is {value}")

def recursive(x,y):
    # multiplication of two integers with recursive call

    if y == 0:
       return 0
    elif y == 1:
       return x
    else:
       return x + recursive(x, y-1)          #LOOP WITH SUM OF SHRINKING Y VALUE

        
if __name__ == '__main__':
    main()
