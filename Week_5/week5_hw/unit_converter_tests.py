from unit_converter import distance, temperature, volume, weight

EPSILON = 1

#TEST FUNCTIONS CALL ORIGINAL FUNCTIONS
def test_distance(value, from_units, to_units, expected):
    #tests distance function WITH expected value
    
    print(f'Testing {value}, from {from_units} to {to_units}')
    actual = distance(value, from_units, to_units)
    return abs(actual - expected) < EPSILON

def test_volume(value, from_units, to_units, expected):
    #tests volume function WITH expected value

    print(f'Testing {value}, from {from_units} to {to_units}')
    actual = volume(value, from_units, to_units)
    return abs(actual - expected) < EPSILON

def test_weight(value, from_units, to_units, expected):
    #tests weight function WITH expected value

    print(f'Testing {value}, from {from_units} to {to_units}')
    actual = weight(value, from_units, to_units)
    return abs(actual - expected) < EPSILON

def test_temperature(value, from_units, to_units, expected):
    #tests temperature function WITH expected value

    print(f'Testing {value}, from {from_units} to {to_units}')
    actual = temperature(value, from_units, to_units)
    return abs(actual - expected) < EPSILON


#CALLS TEST FUNCTION IN ORDER TO COUNT TEST FAILS
def run_distance_tests():
    num_fail = 0
    
    # Test 1: 26m to km. Expected: 0.026
    if (test_distance(26,"m","km",0.026)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: 100mi to m. Expected:160934
    if (test_distance(100,"mi","m",160934)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: 0.00003km to in. Expected: 11.811024 
    if (test_distance(0.0003,"km","in",11.811024)):
         print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 4: 66yd to ft. Expected: 198
    if (test_distance(66,"yd","ft",198)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1
    return num_fail

def run_volume_tests():
    num_fail = 0
    
    # Test 1: 35cup to liters. Expected: 8.044
    if (test_volume(34,"cup","l",8.044)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: 100qt to gal. Expected:25
    if (test_volume(100,"qt","gal",25)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: 0.13gal to cup. Expected: 2.497976
    if (test_volume(0.13,"gal","cup",2.497976)):
         print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 4: 1000qt to l. Expected: 946.353
    if (test_volume(1000,"qt","l",946.353)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1
    return num_fail

def run_weight_tests():
    num_fail = 0
    
    # Test 1: 83lb to kg. Expected: 37.6482
    if (test_weight(83,"lb","kg",37.6482)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: 5ton to oz. Expected:160000
    if (test_weight(5,"ton","oz",160000)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: 1600g to lb. Expected: 3.527396
    if (test_weight(1600,"g","lb",3.527396)):
         print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 4: 16st to kg. Expected: 101.605
    if (test_weight(16,"st","kg",101.605)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1
    return num_fail

def run_temperature_tests():
    num_fail = 0
    
    # Test 1: 83 fahrenheit to celsius. Expected: 28.3333
    if (test_temperature(83,"fahrenheit","celsius",28.3333)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: 100 celsius to fahrenheit. Expected:212
    if (test_temperature(100,"celsius","fahrenheit",212)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: -70 fahrenheit to celsius. Expected: -56.6667
    if (test_temperature(-70,"fahrenheit","celsius",-56.6667)):
         print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 4: -35 celsius to fahrenheit. Expected: -31
    if (test_temperature(-35,"celsius","fahrenheit",-31)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1
    return num_fail

#MAIN CALLS TEST FUNCTIONS THROUGH RUN FUNCTIONS
def main():

    #Calling distance tests
    print('Testing distance functions...\n')
    failures = run_distance_tests()
    if failures == 0:
        print('Everything passed in distance')
    else:
        print('Something went wrong in distance\n\n')
    
    #Calling volume tests
    print('Testing volume functions...\n')
    failures = run_volume_tests()
    if failures == 0:
        print('Everything passed in volume')
    else:
        print('Something went wrong in volume\n\n')

    #Calling weight tests
    print('Testing weight functions...\n')
    failures = run_weight_tests()
    if failures == 0:
        print('Everything passed in weight')
    else:
        print('Something went wrong in weight\n\n')

    #Calling temperature tests
    print('Testing temperature functions...\n')
    failures = run_temperature_tests()
    if failures == 0:
        print('Everything passed in temperature')
    else:
        print('Something went wrong in temperature\n\n')
    
main()
