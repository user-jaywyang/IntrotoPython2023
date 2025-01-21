def main():
    # Write a program that reads through any dictionary like this and prints the following: 
    # (a) All the users whose phone number ends in an 8 
    # (b) All the users that don’t have an email address listed 
    sample_dict = sample()

    print("Part A")
    for x in range(len(sample_dict)):
        num_string = sample_dict[x]['phone']   #phone
        if num_string[-1] == "8":              #check for 8
            print(sample_dict[x]['name'])      #print name
    print("\n")

    
    print("Part B")
    for x in range(len(sample_dict)):
        if sample_dict[x]['email'] == "":     #check for no email
            print(sample_dict[x]['name'])     #print name


def sample():
    #creates a sample list of dictionarys
    sample_dict = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
                   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
                   {'name':'Princess', 'phone':'555-3141', 'email':''},
                   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'},
                   {'name':'George', 'phone':'555-9994', 'email':'george@mail.net'},
                   {'name':'Travis', 'phone':'555-2648', 'email':''},
                   {'name':'Marcus', 'phone':'555-6565', 'email':'marcus@mail.net'},
                   {'name':'Jeremy', 'phone':'555-5042', 'email':''},
                   {'name':'Dean', 'phone':'555-2673', 'email':''},
                   {'name':'Arthur', 'phone':'555-1418', 'email':'arthur@mail.net'}]
    return sample_dict    


if __name__ == '__main__':
    main()
