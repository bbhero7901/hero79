from flask import Flask, jsonify, render_template
import psycopg2 as dbapi2

application = Flask(__name__)
db = dbapi2.connect (database="dafambackend", user="postgres", password="b4nkb4ntul2012")
cur = db.cursor()

def check_login(nama, password):
    query = "select id, nama from coba where nama='{}' and password='{}'".format(nama, password)
    cur.execute(query)
    rows = cur.fetchall()
    return len(rows) > 0

@application.route('/login/<nama>/<sandi>')
def login(nama, sandi):
    hasil = {}
    if check_login(nama, sandi):
        hasil['pesan']='masukan benar'
        hasil['succeded'] = True
    else:
        hasil['pesan']='masukan salah'
        hasil['succeded'] = False
    return jsonify(hasil)

@application.route('/get_users')
def get_users():
    cur.execute ("SELECT id, nama, password FROM coba");
    rows = cur.fetchall()
    users = []
    for i, row in enumerate(rows):
        users.append({'id': row[0]})
        users.append({'nama': row[1]})
        users.append({'password': row[2]})

    return jsonify(data=users)

@application.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    application.run(debug=True)
