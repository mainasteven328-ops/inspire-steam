#name: steve lawrence
#date:13/2/2026
#programme: to calculate arithmetic progression

#calculating the nth term

a = int(input("enter the number of terms :"))
n = int(input ("enter the number of terms:"))
d = int(input("enter the common difference :"))
nth_term= a+(n-1)*d

sn= int(n /2 *((2*a + (n-1)*d)))

print (f"the nth term is : {nth_term}")
print(f"the sum of terms is : {sn}")