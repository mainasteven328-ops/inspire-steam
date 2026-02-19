# name : steve lawrence
# date: 19/2/2026
# program : to define

...
def cook_egg():
    oil = "20 ml"
    pan=True
    moto = True
    eggs = 2
    print(f"the pan is {pan}, and the fire is {moto},add {oil} amount of oil and cook {eggs} eggs")

print("here is statement 1")    
print("here is statement 2")

cook_egg()
print("here is statement 3")

# ride fare creating function

def create_fare(route,distance, is_rush_hour):
  if is_rush_hour == True:
    fare = distance * 10
    fare= fare * 1.5
  print(f"the fare on route {route}, is {fare}")

  return fare


  
  returned_fare = create_fare("Juja-Allsops",7,True)
  print(f"the returned fare is{returned_fare}")


 


# passing a list as a parameter
def write_all_interests(interests):
  for interest in interests:
    print(f" i am interested in {interests}")

all_interests = {"playing foootball", "trading", "ragebaiting", "teachimg bro on puhbending like the king of jungle i am"}  

write_all_interests(all_interests)
