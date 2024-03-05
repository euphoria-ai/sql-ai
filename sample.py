import sqlite3 as sq

connection = sq.connect("food.db")
cursor = connection.cursor()

table_info="""
create table if not exists PEOPLE (
    NAME VARCHAR(25), 
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    SCORE INT
);
"""

cursor.execute(table_info)
cursor.executescript(
    """insert into PEOPLE values('Paul','Data Science', 'A', 10);
    insert into PEOPLE values('Alex','Data Science', 'B', 10);
    insert into PEOPLE values('Joshua','Data Science', 'A', 10);
    insert into PEOPLE values('Derik','History', 'A', 10);
    insert into PEOPLE values('Jason','History', 'A', 10);
    insert into PEOPLE values('Maya','History', 'A', 10);"""
)

data = cursor.execute(
    """select * from PEOPLE """
)
for i in data:
    print(i)
