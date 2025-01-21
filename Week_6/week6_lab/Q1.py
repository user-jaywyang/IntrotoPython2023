def main():
    #A program that repeatedly asks the user to enter product names and prices. Store 
    #all of these in a dictionary whose keys are the product names and whose values are the prices. 
    #When the user is done entering products and prices, allow them to repeatedly enter a 
    #product name and print the corresponding price or a message if the product is not in the dictionary. 

    inventory = initialize()  #create dictionary

    ask(inventory)  #search product and find price

    
def initialize():
    # asks the user to create dictionary of products and prices

    inventory = {}                                                          
    num = int(input("Hello! How many products would you like to input? "))

    for i in range(num):
        product = (input("Enter product name: ")) 
        product = product.upper()    #change to upper case to insure user input compatibility

        price = float(input("Enter product price: "))     
        inventory[product] = price    #asign price to product

    return inventory


def ask(inventory):
    x = input("What price would you like to check? (Type 'exit' to stop!)\n ")
    x = x.upper()      #change to upper case to insure user input compatibility
    
    if  x in inventory:      
        print(f"{x} is {inventory[x]}!")  
        ask(inventory)     #recursive to repeat inquiry

    elif x == "EXIT":
        return             

    elif  x not in inventory:
        print("Product not in inventory!")
        ask(inventory)  #recursive to repeat inquiry
    

if __name__ == '__main__':
    main() 
