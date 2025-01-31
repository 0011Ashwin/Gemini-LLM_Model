import sqlite3

# Connect to sqlite 
connection = sqlite3.connect('student.db')

# create a curosr object to insert records, create table, retrieve
cursor = connection.cursor()


# create the table 
table_info = """
Create table STUDENT(NAME VARCHAR(15),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

#Insert Some more records into

cursor.execute(''' Insert Into Student values('Ashwin','Data Science','A',90) ''')
cursor.execute(''' Insert Into Student values('Hariom','Andorid','D',90)''')
cursor.execute(''' Insert Into Student values('Arjun','Web_development','D',89)''')
cursor.execute(''' Insert Into Student values('Rahul','Data Science','A',90)''')
cursor.execute(''' Insert Into Student values('Raj','Data Science','A',90)''')


# display all the results

print("The inserted records are")

data = cursor.execute('''Select * from Student''')

for row in data:
    print(row)
    
# Close the connection
connection.commit()
connection.close()
    


