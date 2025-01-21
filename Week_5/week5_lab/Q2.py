
def main ():
    num = input("Enter a number and Ill give you the sum of its digits: ")
    sum_digits(num)

def sum_digits(x):
    #given an integer num and returns the sum of the digits of num. 

    sum = 0                           # cache for loop
    for y in range(len(x)):                    
        sum = sum + int(x[y])         # cast string index to int and add to cache
    
    print(sum)

main()
