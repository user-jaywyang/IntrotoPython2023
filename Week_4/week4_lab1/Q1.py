def main():
    #Ask for input string, returns various print statements

    string = input("Please enter a word or phrase: ")
    B_CONSTANT = 10                #magic number in part b
    G_CONSTANT = 7                 #magic numbHeer in part g
    length = len(string)           #string length as constant

    print (length)                 #a) total number of characters in string
    print (string * B_CONSTANT)         #b) string repeated 10 times
    print (string[0])                   #c) first character of string
    print (string[0:3])                 #d) first three characters of string
    
    new_stringf = ""                    #f) string backwords
    for x in range(length):        
        new_stringf= string[x] + new_stringf
    print(new_stringf)
    
    if len(string) >= G_CONSTANT:       #g) 7th character, otherwise message
        print(string[G_CONSTANT - 1])
    else:
        print("Not enough characters to print seventh.")
 
    print (string[1:length-1])          #h) first and last character removed
    
    print (string.upper())              #i) all uppercase
    
    new_stringj = ""                    #j) replace all e's with a's
    for x in range(length):
        if string[x] == "a":
            new_stringj = new_stringj + "e"
        elif string[x] == "A":
            new_stringj = new_stringj + "E"
        else:
            new_stringj = new_stringj + string[x]
    
    print(new_stringj)

main()
