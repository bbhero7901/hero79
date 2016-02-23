from flask import Flask, jsonify, render_template

application = Flask(__name__)

@application.route('/login/<nama>/<sandi>')
def login(nama, sandi):
    hasil = {}
    if nama == 'gembul' and sandi == '123':
        hasil['pesan']='masukan benar'
        hasil['succeded'] = True
    else:
        hasil['pesan']='masukan salah'
        hasil['succeded'] = False
    return jsonify(hasil)
@application.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    application.run(debug=True)
