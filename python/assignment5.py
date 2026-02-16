#name: steve lawrence
#date:16/2/2026
#programme: to calculate income tax of an employee
 
salary = int(input("enter your gross salary : "))

if salary < 50000 :
    tax = (2.5 / 100)* salary
    net_salary =salary - tax

if 50000< salary <= 100000:
    tax = (4.5 / 100)* salary
    net_salary =salary - tax

if salary >= 100000 :
    tax = (7.5/100)* salary
    net_salary = salary - tax
print (f"gross salary = {salary}")
print(f"net_salary = {net_salary}")
print(f"tax = {tax}")
 
