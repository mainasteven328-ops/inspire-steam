#name : steve lawrence
#date : 24.02.2026
# program : to show file operations

# create new file
new_file = open("student_data.txt","r+")

# write to new file
new_file.write("student name : king of the jungle osns , ID : 9845867 , email : kotj@gmail.com")

# read new file
data = new_file.read()
print(data)
new_file.close()

# delete file


# use os
import os
os.remove("remove.txt")

# delete folder
os.rmdir("folder")