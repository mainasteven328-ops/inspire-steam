# b\name : steve lawrence 
# date : 17/2/2026
# program: to format output

name = "steve lawrence"

weight = 70 # weight in kilograms

fav_team = "mancity"

height 175.98  # height in centimetres

# 1. format using print f(f"{}")

print ( f "my name is {name} and i am weight {weight} in kgs")


# usinf f string 

msg = f" my name is {name} and i support {fav_team}"
print (msg)

#3 using {} and .format()
print("my name is {0} and i am {1}cm tall". format (name,height))

#4 using output specifiers %s -strings %f- float, %s - strings
import math
print ("i support %s" fav_team)
