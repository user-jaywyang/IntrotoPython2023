def main():
    # Design a function that uses recursion to raise a number to a power. The 
    # function should accept two arguments: the number to be raised, and the 
    # exponent. Assume the exponent is a nonnegative integer. 
    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))
    value = power(x,y)
    print(value)

def power(x,y):
    #returns x to the power of y with recursive call

    if y == 0:
       return 1
    elif y == 1:
       return x
    else:
       return x * power(x, y-1)             #LOOP WITH PRODUCT OF SHRINKING Y VALUE

if __name__ == '__main__':
    main()
