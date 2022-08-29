import sys
import pyodbc


connGG = pyodbc.connect('Driver={SQL SERVER};'
                        'Server=10.110.10.29;'
                        'Database=DB-TG;'
                        'UID=sa;'
                        'PWD=Aa123456;'
                        'Trusted_Connection=yes;''autocommit=True')


cursor = connGG.cursor()

#connGG.setdecoding(pyodbc.SQL_CHAR, encoding='utf-16')
#connGG.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-16')
#connGG.setencoding(encoding='utf-16')

#SQLQuery = ("""
#                SELECT TG_message_id, TG_message_text, TG_message_is_deleted, TG_message_is_forwarded, TG_message_file, TG_message_file_content
#                FROM [DB-TG].dbo.[useranon]
#
#
#            """) #5276890896


useranon = "SELECT * FROM useranon"
cursor.execute(useranon)


SQLinsert = '''INSERT INTO useranon (Int_ID, TG_message_id, TG_message_text, TG_message_is_deleted, TG_message_is_forwarded, TG_message_is_file, TG_message_file_content)
                VALUES (4,?,?,1,0,0,0);'''

#cursor.execute('''INSERT INTO useranon (TG_message_id, TG_message_text, TG_message_is_deleted, TG_message_is_forwarded, TG_message_is_file, TG_message_file_content)
#                VALUES (?,?,?,?,?,?);''')



results  = cursor.fetchall() #[0]
for row in results:
    Int_ID = row[0]# row(int[0])
    TG_message_id = row[1]
    TG_message_text = row[2]
    TG_message_is_deleted = row[3]
    TG_message_is_forwarded = row[4]
    TG_message_is_file = row[5]
    TG_message_file_content = row[6]

    values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    print(Int_ID, TG_message_id, TG_message_text, TG_message_is_deleted, TG_message_is_forwarded, TG_message_is_file, TG_message_file_content)
#    cursor.execute(SQLZapros)
    cursor.execute(SQLinsert, results, values)


connGG.commit()

cursor.execute('SELECT * FROM useranon')

for row in cursor:
    print(row)


#for statement in SQLZapros.split(';'):
#    with connGG.cursor() as cur:
#cursor.execute(statement)
#cursor.execute(SQLZapros)
results = cursor.fetchall()
connGG.close()


#cursor.execute(SQLzapros)
#connGG.commit() скажем не работает

#cursor.execute(SQLQuery)

#results = cursor.fetchall() # работает

#cursor.execute('''INSERT INTO (TG_message_id, TG_message_text, TG_message_is_deleted)
#                           VALUES
#                           404, 'тест ыыыытест', 1 ''')

#TG_message_id=int(input()) Не знаю для чего
#print("Enter first Name")
#TG_message_text=input()
#print("Enter last Name")
#TG_message_is_deleted=int(input())
#print("Enter message_is_deleted")

#SQLCommand = ("INSERT INTO useranon(TG_message_id, TG_message_text, TG_message_is_deleted) VALUES (?,?,?)")
#Values = [TG_message_id, TG_message_text, TG_message_is_deleted]
#cursor.execute(SQLCommand,Values)
#connGG.commit() Не знаю для чего


#for row in cursor:
#    print(row.TG_message_id, row.TG_message_text, row.TG_message_is_deleted) #worked





#rows = cursor.fetchall()
#for row in rows:
#    print(row.TG_message_id, row.TG_message_text, row.TG_message_is_deleted) #all tables

#for row in results:
#    TG_message_id = row[0]
#    TG_message_text = row[1]
#    TG_message_is_deleted = row[2]


#print(TG_message_id)
#print(TG_message_text)
#print(TG_message_is_deleted)


#print(results)

#read(connGG)
#create(connGG)
#update(connGG)
#delete(connGG)



#
#def read(connGG):
#    print("Read")
#    cursor = connGG.cursor
#    cursor.execute('SECELT * from [DB-TG].dbo.[5276890896]')
#    for row in cursor:
#        print(f'row = {row}')
#    print()
#
#def create(connGG):
#    print("Create")
#    cursor = connGG.cursor
#    cursor.execute(
#        'INSERT INTO [DB-TG].dbo.[5276890896](a,b) values (?,?);',
#        (3232, 'catzozo')
#   )
#    connGG.commit()
#    read(connGG)
