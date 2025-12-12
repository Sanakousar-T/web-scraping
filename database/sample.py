import sqlite3
conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
# step: 1
# cursor.execute("create table employee(name varchar(32), designation varchar(32));")
# cursor.execute("insert into employee values('sana','software test engineer');")
# step: 2
"""
for i in range(10):
    name = input('enter the name:')
    des = input('enter the designation:')
    cursor.execute(f"insert into employee values('{name}','{des}');")
    conn.commit()
"""
# step: 3
"""
data = cursor.execute("select * from employee;")
for i in data:
    print(i)
"""