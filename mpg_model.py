#!/usr/bin/env python3

# display a welcome message
print("Rectangle_console_application")
print()

# get input from the user
length = float(input("Enter Length:\t"))
width = float(input("Enter Width:\t"))

# calculate the Area and Perimeter 
Area = length * width
Perimeter = width * 2 + length * 2 
            
# format and display the result
print("Area:\t" + str(Area))
print("Perimeter: " +str(Perimeter))
print()
print("Bye")


