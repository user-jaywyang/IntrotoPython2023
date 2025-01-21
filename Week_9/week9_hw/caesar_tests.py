import caesar

#TEST FUNCTIONS CALL ORIGINAL FUNCTIONS
def test_caesar_encrypt(plain, key, expected):
    #tests encrypt function WITH expected value
    
    print(f'Testing caesar encryption, from {plain} to {expected}')
    actual = caesar.Caesar(plain)
    actual = actual.encrypt(key)
    print (f'Result: {actual}')
    return actual == expected

def test_caesar_decyrypt(cypher, key, expected):
    #tests decyrypt function WITH expected value

    print(f'Testing caesar encryption, from {cypher} to {expected}')
    actual = caesar.Caesar(cypher)
    actual = actual.decyrypt(cypher, key)
    print (f'Result: {actual}')

    return actual == expected

#CALLS TEST FUNCTION IN ORDER TO COUNT TEST FAILS
def run_caesar_encrypt():
    
    # Test 1:  
    if (test_caesar_encrypt('Prof Jump is crazy to thi nk we can do this', 3, 'SURIMXPSLVFUDCBWRWKLQNZHFDQGRWKLV')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 2:  
    if (test_caesar_encrypt('defend the east wall of the castle', 1, 'EFGFOEUIFFBTUXBMMPGUIFDBTUMF')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 3:  
    if (test_caesar_encrypt('abcdefghijklmnopqrstuvwxyz', 1, 'BCDEFGHIJKLMNOPQRSTUVWXYZA')):
         print('PASSED! :)')
    else:
        print('FAILED :(')


def run_caesar_decyrypt():
    
    # Test 1: 
    if (test_caesar_decyrypt('SURIMXPSLVFUDCBWRWKLQNZHFDQGRWKLV', 3, 'PROFJUMPISCRAZYTOTHINKWECANDOTHIS')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 2: 
    if (test_caesar_decyrypt('EFGFOEUIFFBTUXBMMPGUIFDBTUMF', 1, 'DEFENDTHEEASTWALLOFTHECASTLE')):
        print('PASSED! :)')
    else:
        print('FAILED :(')

    # Test 3:  
    if (test_caesar_decyrypt('BCDEFGHIJKLMNOPQRSTUVWXYZA', 1, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
         print('PASSED! :)')
    else:
        print('FAILED :(')


#MAIN CALLS TEST FUNCTIONS THROUGH RUN FUNCTIONS
def main():

    #Calling ENCRYPT tests
    print('Testing encrypt functions...\n')
    run_caesar_encrypt()
    
    
    #Calling DECYRYPT tests
    print('Testing decyrypt functions...\n')
    run_caesar_decyrypt()
    

main()
