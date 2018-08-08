import os
import datetime

#1
'''
file_path = open("file_path.txt", 'w')
file_path.write(os.getcwd())
file_path.close()


file_list = open("file_list.txt", "w")
for i in os.listdir():
    file_list.write(i)
    file_list.write("\n")
file_list.close()
'''

#2
'''
file_now = open("file_now.txt", 'w')
file_now.write(str(datetime.datetime.now()))
file_now.close()
'''

#3
'''
file_username_password = open("file_username_password.txt", 'r')
username_password_dict = {}
for line in file_username_password:
    username_password_dict[line.split(":")[0]] = line.split(":")[1][:-1]
print (username_password_dict)
file_username_password.close()

print ("Please enter USERNAME")
entered_username = input()

if entered_username in username_password_dict:
    print ("Please enter PASSWORD")
    entered_password = input()
    if entered_password == username_password_dict[entered_username]:
        print("ACCESS GRANTED")
    else:
        print("INCORRECT PASSWORD")
else:
    print("would like to create a new username?")
    if input() == "yes":
        print ("please enter a new username")
        new_username = input()
        print ("please enter a new password")
        new_password = input()

        file_username_password = open("file_username_password.txt", 'w')
        username_password_dict[new_username] = new_password
 
print (username_password_dict)

file_username_password = open("file_username_password.txt", 'w')
for i in username_password_dict:
    file_username_password.write(i+':'+username_password_dict[i]+'\n')
file_username_password.close()
'''

#4
file_sumall = open("sumall_file.txt", 'r')
def sumAll(filename):
    integer_list = []
    for line in filename:
        integer_list = line.split(' ')[:-1]
    print (integer_list)

sumAll(file_sumall)