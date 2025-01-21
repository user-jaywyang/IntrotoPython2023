def main():
    #main
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    first_diff(str1, str2)
    

def first_diff(str1, str2):
    #Given two strings and returns the first location in which the strings differ. 
    #If the strings are identical, it should return -1. 

    if str1 == str2:                    #identical check
        print(-1)

    else:
        for x in range(len(str1)):      #loop for string index checks          
            if str1[x] != str2[x]:      
                print(x)
                return
                
main()
