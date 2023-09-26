print("*** Welcome ***") #Welcome message
print("")#Space between lines
r = float(input("What is the radius of the circle? ")) #Input information of user

d = 2*r #Diameter calculation
c = 2*(3.14)*r #Circumference calculation
a = (3.14)*r*r #Area calculation

print("") #Space between lines
print("A circle with a radius of " + str(r) + " units will have a diameter of " + str(d)  + " units, a circumference of " + str(c) + " units and an area of " + str(a) + " square units.") #Printing results
print("") #Space between lines
print("*** Thank you ***") #Ending program