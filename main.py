import sys
import pyodbc


connGG = pyodbc.connect('Driver={SQL SERVER};'
                        'Server=;'
                        'Database=DB-TG;'
                        'UID=sa;'
                        'PWD=Aa123456;'
                        'Trusted_Connection=yes;''autocommit=True')


cursor = connGG.cursor()

useranon = "SELECT * FROM useranon"
cursor.execute(useranon)


SQLinsert = '''INSERT INTO useranon (Int_ID, TG_message_id, TG_message_text, TG_message_is_deleted, TG_message_is_forwarded, TG_message_is_file, TG_message_file_content)
                VALUES (?,?,?,?,?,?,?);'''


results = cursor.fetchall() #[0] fetchall
for row in results:
    Int_ID = row[0]# row(int[0])
    TG_message_id = row[1]
    TG_message_text = row[2]
    TG_message_is_deleted = row[3]
    TG_message_is_forwarded = row[4]
    TG_message_is_file = row[5]
    TG_message_file_content = row[6]

    values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
#   print(Int_ID, TG_message_id, TG_message_text, TG_message_is_deleted, TG_message_is_forwarded, TG_message_is_file, TG_message_file_content)
    print(values)
#cursor.execute(SQLinsert, results()) # не работает
cursor.execute("SELECT * from useranon") #работает, но что-то не так...

connGG.commit()

#cursor.execute('SELECT * FROM useranon')

#def read(connGG):
#    print("Read")
#    cursor = connGG.cursor
#    cursor.execute('SECELT * from dummy')
#    for row in cursor:
#        print(f'row = {row}')
#    print()


#def create(connGG):
#    print("Create")
#    cursor = connGG.cursor
#    cursor.execute(
#        'INSERT INTO dummy(a,b) values (?,?);',
#        (3232, 'catzozo')
#    )
#    connGG.commit()
#    read(connGG)


#def update(connGG):
#    print("update")
#    cursor = connGG.cursor
#    cursor.execute(
#        'UPDATE dummy set b = ? where a = ?;',
#        ('dogzozo', 3232)
#    )
#    connGG.commit()
#    read(connGG)

#def delete(connGG):
#    print("Delete")
#    cursor = connGG.cursor
#    cursor.execute(
#        'DELETE FROM dummy WHERE a > 5'
#    )
#    connGG.commit()
#    read(connGG)


#read(connGG)
#create(connGG)
#update(connGG)
#delete(connGG)

connGG.close()
