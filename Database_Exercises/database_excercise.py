import sqlite3

"""Create the youngwonks database, create cartoon character table, and insert cartoon characters """
# Create database and connect to it
#  The object create_cursor is used to send commands to the database
conn = sqlite3.connect('youngwonks.db')
cursor = conn.cursor()

# In case there is an old instance of table, cartoon, delete it
# If you are sharing a computer with other students they may have already created one
try:
    cursor.execute('''DROP TABLE cartoon''')
except Exception as exception:
    print("Error, Please ask instructor for help, Exception is:", exception)

# Create the table
cursor.execute('''CREATE TABLE cartoon(firstName text, lastName text, address text, city text, age integer)''')

# Insert the characters
characters = [('Mickey', 'Mouse', '1400 Disney Way', 'Anaheim', 73),
              ('Minnie', 'Mouse', '1400 Disney Way', 'Anaheim', 41),
              ('Bugs', 'Bunny', '92 Star Way', 'New York', 37),
              ('Donald', 'Duck', '1400 Disney Way', 'Anaheim', 54),
              ('Bat', 'Man', '91 Robin Street', 'Gotham City', 26)]\

cursor.executemany('INSERT INTO cartoon VALUES (?,?,?,?,?)', characters)

# Write the data to database
conn.commit()

# Print rows that was just created
print("Created table cartoon with the following contents: ")
row_number = 1
print("        First Name  Last Name   Address           City    Age ")


for row in cursor.execute('SELECT * FROM cartoon'):
    print("Row",row_number,"=", row)
    row_number = row_number + 1

print ('\n', cursor.execute('''SELECT firstName from cartoon where lastName = "Duck" ''').fetchall(),
       cursor.execute('''SELECT lastName FROM cartoon WHERE firstName = "Donald" ''').fetchall(),
       cursor.execute('''SELECT age FROM cartoon WHERE firstName = "Donald" ''').fetchall())

# Done, so close access to the database
cursor.close()