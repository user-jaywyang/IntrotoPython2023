def main():
    # Assume a file containing a series of integers is named numbers.txt and exists 
    # on the computer’s disk. Write a program that calculates the average of all the numbers stored in the file.    
    # In addition, it should also do the following: 
    # • It should handle any IOError exceptions that are raised when the file is opened and data is read from it. 
    # • It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.

    file = input("What file would like to check? \n")
    
    try:
        infile = open(file, "r")                       #OPEN FILE
    except IOError:                                    #CHECK FOR VALID FILE INPUT
        print("\n ERROR:File is not found \n")
        main()                                         #RECURSIVE BACK TO ASK
    else:
        cache = 0                                      #SUM
        count = 0                                      #AMOUNT OF INTEGERS

        for line in infile:
            try:
                cache += int(line)
                count += 1
            except ValueError:                         #CHECK FOR INTEGERS IN FILE
                print(f"\nERROR: File {file} includes an non integer value.\n")
                return

        infile.close()                                 #CLOSE FILE
        avg = cache/count
        print(f"\nThe average of integers in file is {avg}")


if __name__ == '__main__':
    main()
