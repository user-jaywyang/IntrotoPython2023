
def main():
# Write a program that asks the user for the name of a file. The program 
# should display only the first five lines of the file’s contents. If the file contains 
# less than five lines, it should display the file’s entire contents.  
    file = input("What file would you like to preview five lines? \n ")
    
    #open file and assign to variable
    infile = open(file, "r")

    nuline1 = infile.readline()
    line1 = line1.rstrip('\n')

    line2 = infile.readline()
    line2 = line2.rstrip('\n')

    line3 = infile.readline()
    line3 = line3.rstrip('\n')

    line4 = infile.readline()
    line4 = line4.rstrip('\n')

    line5 = infile.readline()
    line5 = line5.rstrip('\n')


    #close file
    infile.close()

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)



if __name__ == '__main__':
    main()
