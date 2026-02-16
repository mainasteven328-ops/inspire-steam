# name : steve lawrence
# date : 12/02/2026
#programme: programme to use for loops in physics

 # sample data as a list of lists
import math 

print("|______________________________________|")
print("| angle |  sin  | cos  |  tan  |")

print("|_____________________________________|")

for angle in range (-180,181,30):
      rad = math.radians(angle)
      sin_val = round(math.sin(rad), 4)
      cos_val = round(math.cos(rad), 4)

      if angle == 180 or angle == -180 :
            tan_val = "undefined"
            print (f"(angle : {angle:5}) | (sin_val:{sin_val:8.4f}) | (cos_val:{cos_val:8.4f}) | (tan_val:{tan_val:8})")
            
            tan_val = round (math.tan(rad),4)
            print (f"| {angle:5} | {sin_val:8.4f} | {cos_val:8.4f} | {tan_val: 8} |")
            print("|____________________________________|")



#print the table with a grid format for  better readability



   


 