import railfence

#TEST FUNCTIONS CALL ORIGINAL FUNCTIONS
def test_railfence_encrypt(plain, key, expected):
    #tests encrypt function WITH expected value
    
    print(f'Testing railfence encryption, from {plain} to {expected}')
    actual = railfence.Railfence(plain)
    actual = actual.encrypt(key)
    print (f'Result: {actual}')
    return actual == expected

def test_railfence_decyrypt(cypher, key, expected):
    #tests decyrypt function WITH expected value

    print(f'Testing railfence encryption, from {cypher} to {expected}')
    actual = railfence.Railfence(cypher)
    actual = actual.decyrypt(cypher, key)
    print (f'Result: {actual}')

    return actual == expected

#CALLS TEST FUNCTION IN ORDER TO COUNT TEST FAILS
def run_railfence_encrypt():
    
    # Test 1:  
    if (test_railfence_encrypt('Prof Jump is crazy to thi nk we can do this', 4, 'PMAHCHRUPRZTIEATIOJICYONWNOSFSTKD')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 2:  
    if (test_railfence_encrypt('defend the east wall of the castle', 3, 'DNETLHSEEDHESWLOTEATEFTAAFCL')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 3:  
    if (test_railfence_encrypt('defend the east wall of the castle', 4, 'DTTFSEDHSWOTATFNEAALHCLEELEE')):
         print('PASSED! :)')
    else:
        print('FAILED :(')


def run_railfence_decyrypt():
    
    # Test 1: 
    if (test_railfence_decyrypt('PMAHCHRUPRZTIEATIOJICYONWNOSFSTKD', 4, 'PROFJUMPISCRAZYTOTHINKWECANDOTHIS')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 2: 
    if (test_railfence_decyrypt('DNETLHSEEDHESWLOTEATEFTAAFCL', 3, 'DEFENDTHEEASTWALLOFTHECASTLE')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 3:  
    if (test_railfence_decyrypt('DTTFSEDHSWOTATFNEAALHCLEELEE', 4, 'DEFENDTHEEASTWALLOFTHECASTLE')):
         print('PASSED! :)')
    else:
        print('FAILED :(')


#MAIN CALLS TEST FUNCTIONS THROUGH RUN FUNCTIONS
def main():

    #Calling ENCRYPT tests
    print('Testing encrypt functions...\n')
    run_railfence_encrypt()
    
    
    #Calling DECYRYPT tests
    print('Testing decyrypt functions...\n')
    run_railfence_decyrypt()
    

main()
