from math import pi

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))
fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
