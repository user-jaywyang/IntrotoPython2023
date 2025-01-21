
def main():
    # Assume a file containing a series of names (as strings) is named names.txt 
    # and exists on the computer’s disk. Write a program that displays the number of 
    # names that are stored in the file. 
    
    file = input("What file would like to check? \n")
    
    #open file and assign to variable
    infile = open(file, "r")

    count = 0                      #cache
    file_list = infile.readlines()     #list of names by each line

    for x in file_list:                #AKA length of file lines
        if infile.readline()!= '\n':   #check if x is empty line
            count += 1                 


    #close file
    infile.close()

    print(f"There are {count} names in this file.")

if __name__ == '__main__':
    main()
