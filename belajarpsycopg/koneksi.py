import psycopg2 as dbapi2


db = dbapi2.connect (database="dafambackend", user="postgres", password="b4nkb4ntul2012")
cur = db.cursor()

#clear data
cur.execute ("DELETE FROM coba")

#insert data
insert = "insert into coba(id, nama, password) values('{}', '{}','{}')"
sql = insert.format('123', 'hero', 'jugarahasia')
print(sql)
cur.execute(sql)
cur.execute(insert.format('456', 'koko', 'rahasia'))

cur.execute ("SELECT * FROM coba");
rows = cur.fetchall()
for i, row in enumerate(rows):
    print("Row", i, "value = ", row)

db.commit()
cur.close()
db.close()


def check_login(nama, password):
    query = "select id, nama from coba where nama='{}' and password='{}'".format(nama, password)
    cur.execute(query)
    rows = cur.fetchall()
    return len(rows) > 0

db = dbapi2.connect (database="dafambackend", user="postgres", password="b4nkb4ntul2012")
cur = db.cursor()

# selanjutnya pergunakan fungsi check_login tersebut
print(check_login('koko', 'rahasia'))
