import sqlite3 as sq

connection = sq.connect("student.db")
cursor = connection.cursor()

table_info="""
create table if not exists STUDENT(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25),
    SECTION VARCHAR(25)
);
"""

cursor.execute(table_info)
cursor.executescript(
    """insert into STUDENT values('Paul','Data Science', 'A');
    insert into STUDENT values('Alex','Data Science', 'B');
    insert into STUDENT values('Joshua','Data Science', 'A');
    insert into STUDENT values('Derik','History', 'A');
    insert into STUDENT values('Jason','History', 'A');
    insert into STUDENT values('Maya','History', 'A');"""
)

data = cursor.execute(
    """select * from STUDENT"""
)
for i in data:
    print(i)
