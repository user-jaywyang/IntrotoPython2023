from msilib.schema import File


def main():


    #open file and assign to variable
    infile = open("class7.txt", "r")

    line1 = infile.readline()
    line1 = int(line1.rstrip('\n'))

    line2 = infile.readline()
    line2 = int(line2.rstrip('\n'))

    line3 = infile.readline()
    line3 = int(line3.rstrip('\n'))

    #close file
    infile.close()

    sum = line1 + line2 + line3
    print(sum)

    infile = open("class7.txt", "a")
    infile.write(str(sum))
    infile.close()
    
    



if __name__ == '__main__':
    main()
