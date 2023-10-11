#Lola Weis
#CS-175
#Resaurant

vegetarian= str(input("Is anyone in your party vegetarian? "))
vegan= str(input("Is anyone in your party vegan? "))
gluten= str(input("Is anyone in your party gluten-free? "))

if vegetarian=="Yes" or "yes":
    if vegan=="Yes" or "yes":
        if gluten=="Yes" or "yes":
            print("The Chef's Kitchen\n" "Corner Cafe")
        else:
            print("The Chef's Kitchen\n" "Corner Cafe")
    else:
        if gluten=="Yes" or "yes":
            print("Main Street Pizza Company\n" "The Chef's Kitchen\n" "Corner Cafe")
        else:
            print("Main Street Pizza Company\n" "The Chef's Kitchen\n" "Corner Cafe\n" "Mama's Fine Italian")

else:
    if vegan=="Yes" or "yes":
        if gluten=="Yes" or "yes":
            print("The Chef's Kitchen\n" "Corner Cafe")
        else:
            print("The Chef's Kitchen\n" "Corner Cafe")
    else:
        if gluten=="Yes" or "yes":
            print("Main Street Pizza Company\n" "The Chef's Kitchen\n" "Corner Cafe")
        else:
            print("Main Street Pizza Company\n" "The Chef's Kitchen\n" "Corner Cafe\n" "Mama's Fine Italian\n" "Joe's Gourmet Burgers")
                

