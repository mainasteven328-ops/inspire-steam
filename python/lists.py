#name : steve lawrence
#date : 16.02.2026
# program : to show lists in python

friends = ["rachel", "phoebe", "ross","chandler","monica","joey"]
print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("jack")
print(friends)

new_friends = ["joe","unc","gentrix","kimbery","bena","joo mama"]
print(len(new_friends))

students = friends + new_friends
print(students)
students.insert(9,"puh")
print(students)
students.extend("osns")
students.remove("joey")
print(students)

new_students = students.copy()
print(new_students)
print(students.count("joo mama"))


