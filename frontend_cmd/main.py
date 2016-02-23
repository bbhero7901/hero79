import requests

alas = input('Alas segitiga :')
tinggi = input('Tinggi segitiga :')
url = 'http://127.0.0.1:5000/hitung_as_json/{}/{}'.format(alas, tinggi)
print('Communicating with backend server.. please wait')
r = requests.get(url)
d = r.json()
print ('Result from server', d['luas_segitiga'])
