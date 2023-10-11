#CS175
#Lola Weis
#restaurant version 2

vegetarian=False
vegan=False
gluten_free=False
askagain=True
while askagain== True:
    vegetarianif = str(input("Is anyone in your party vegetarian? ").lower())
    if vegetarianif== "yes":
        vegetarian=True
    veganif= str(input("Is anyone in your party vegan? ").lower())
    if veganif== "yes":
        vegan=True
    glutenfreeif= str(input("Is anyone in your party gluten free? ").lower())
    if glutenfreeif== "yes":
        gluten_free=True
                    
    print("Here are your restaurant choices: ")

    print("Corner Cafe")
    print("Chefs Kitchen")

    if vegetarian== False and vegan == False and gluten_free== False:
                   print ("Joes Gourmet Burgers")
    if vegan== False and gluten_free==False:
                   print("Mamas Fine Italian")
    if vegan==False:
                   print("Main Street Pizza")

    answer= str(input("Would you like to do another restaurant search? ").lower())
    if answer!="yes":
        askagain=False
print("Thank you for using this program!")
        
