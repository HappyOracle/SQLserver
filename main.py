import sys
import pyodbc


connGG = pyodbc.connect('Driver={SQL SERVER};'
                        'Server=123;'
                        'Database=DB-TG;'
                        'UID=sa;'
                        'PWD=;')


cursor = connGG.cursor()

#connGG.setdecoding(pyodbc.SQL_CHAR, encoding='utf-16')
#connGG.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-16')
#connGG.setencoding(encoding='utf-16')

SQLQuery = ("""
                SELECT TG_message_id, TG_message_text, TG_message_is_deleted
                FROM [DB-TG].dbo.[5276890896] 


            """) #5276890896

cursor.execute(SQLQuery)
results = cursor.fetchall()

cursor.execute('''INSERT INTO (TG_message_id, TG_message_text, TG_message_is_deleted)
                           VALUES 
                           404, 'тест ыыыытест', 1 ''')
connGG.commit()



#for row in cursor:
#    print(row.TG_message_id, row.TG_message_text, row.TG_message_is_deleted) #worked





#rows = cursor.fetchall()
#for row in rows:
#    print(row.TG_message_id, row.TG_message_text, row.TG_message_is_deleted) #all tables

for row in results:
    TG_message_id = row[0]
    TG_message_text = row[1]
    TG_message_is_deleted = row[2]


#print(TG_message_id)
#print(TG_message_text)
#print(TG_message_is_deleted)


#print(results)

#read(connGG)
#create(connGG)
#update(connGG)
#delete(connGG)

connGG.close()


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
