def main():
    #unit conversion function- takes a value and converts it from one unit to another (distance, volume, weight, temperature)

    print("Menu options:\n 1 - distance (cm, m, km, in, ft, yd, mi)\n 2 - volume (l, cup, gt, gal)\n \
3 - weight (oz, lb, ton, g, kg, st)\n 4 - temperature(fahrenheit, celsius)")         #MENU DISPLAY

    unit_choice = input("What type of unit would you like to convert? \nEnter choice: ")   #user chooses unit type

    choice_list = ["distance", "volume", "weight", "temperature"] #unit types

    if unit_choice not in choice_list:       #unit choice CHECK
        print("INVALID CHOICE")
        
    else:
        value = eval(input("Enter value to be converted: "))      #store value and units in variables

        from_units = (input("Enter unit to convert FROM: "))

        to_units = (input("Enter unit to convert TO: "))

        if unit_choice == "distance":                             #unit choice conditionals
            new_value = distance(value,from_units,to_units)

        elif unit_choice == "volume":
            new_value = volume(value,from_units,to_units)

        elif unit_choice == "weight":
            new_value = weight(value,from_units,to_units)

        elif unit_choice == "temperature":
            new_value = temperature(value,from_units,to_units)
            
        if new_value == -1:                                             #unit validity CHECK
            print(f"ERROR: cannot convert {from_units} to {to_units}!")
        
        else:                                                           #FINAL VALUE RETURN
            print(f"The conversion from {value} {from_units} is {new_value} {to_units}!")
        

def distance(value, from_units, to_units):
    #Function for distance conversion, returns converted value, parameters include value to be converted and units from and to

    meterconv = {"cm": 100,                           #unit cache
                "m": 1,
                "km": 0.001,
                "in": 39.370078740157,
                "ft": 3.2808398950131,
                "yd": 1.0936132983377,
                "mi": 0.000621371}

    if from_units not in meterconv or to_units not in meterconv:   #unit CHECK
        return(-1)
    
    else:
        meter_value = value * (1/meterconv[from_units])       #convert value to meter
        return_value = meter_value * meterconv[to_units]      #convert value to new unit
        return(return_value)


def volume(value, from_units, to_units):
    #Function for volume conversion, returns converted value, parameters include value to be converted and units from and to

    literconv = {"l": 1,                            #unit cache
                "cup": 4.2267528377,
                "qt": 1.0566882094, 
                "gal": 0.2641720524}

    if from_units not in literconv or to_units not in literconv:            #unit CHECL
        return(-1)
    
    else:
        liter_value = value * (1/literconv[from_units])        #convert value to liter
        return_value = liter_value * literconv[to_units]       #convert value to new unit
        return(return_value)


def weight(value, from_units, to_units):
    #Function for weight conversion, returns converted value, parameters include value to be converted and units from and to

    poundconv = {"oz": 16,                               #unit cache
                "lb": 1,
                "ton": 0.0005,
                "gr": 453.59237,
                "kg": 0.45359237,
                "st": 0.0714285714}

    if from_units not in poundconv or to_units not in poundconv:    #unit CHECK
        return(-1)
    
    else:
        pound_value = value * (1/poundconv[from_units])      #convert value to pound
        return_value = pound_value * poundconv[to_units]     #convert value to new unit
        return(return_value)


def temperature(value, from_units, to_units):
    #Function for temperature conversion, returns converted value, parameters include value to be converted and units from and to
    temp = ["fahrenheit","celsius"]

    if from_units not in temp:   #unit CHECK
        return(-1)

    elif to_units not in temp:
        return(-1)

    elif from_units == to_units:    #same unit conditional
        return(value)

    else:
        if to_units == "fahrenheit":                      #to fahrenheit conversion
            return_value = ((9/5)*value) + 32
            return(return_value)

        elif to_units == "celsius":                       #to celsius conversion
            return_value = (value - 32) * (5/9)
            return(return_value)

    
if __name__ == '__main__':
    main()
