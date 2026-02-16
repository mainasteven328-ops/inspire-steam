#name: steve lawrence
#date:13/2/2026
#programme: to calculate geometric progression

# calculating nth progression

a = int(input("enter the number of terms:"))
r = int(input("enter the common ratio:"))
n = int(input("enter the number of terms:"))

nth_term = a*(r**n-1)
print (f"the nth term is : {nth_term}")

