def main():
    #takes a word with a letter "a" and returns the letters upto (and including) the first "a" 
    #and the rest on second line

    word = input("Please enter a word with the letter 'a': ")
    new_word = ""
    new_word2 = ""
    spot = word.find("a")                        #get index of first occurance of "a"

 
    for x in range(spot+1):                      #make first string including "a"
        new_word = new_word + word[x]
            
    for y in range(spot+1,len(word)):            #make second string after "a"
        new_word2 = new_word2 + word[y]  
    
    print(new_word)
    print(new_word2)

      
          
main() 
