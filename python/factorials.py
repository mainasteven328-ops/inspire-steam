#name: steve lawrence
#date:16/2/2026
#programme: to calculate factorials of numbers

number= int(input("enter the number x :"))
factorial = 1 # initialize factorial as 1
for x in range(1,number + 1):

    factorial *= x
print(f"{number}! = {factorial}")