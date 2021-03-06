from flask import Flask, render_template, request, flash
from translate import *

app = Flask(__name__)

# default route yang akan dijalankan
@app.route('/')
def home() :
    return render_template('index.html', language = 'indo', method = 'bm')

# akan dijalankan setelah submit form
@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST' :
        # mengambil data hasil input form
        kata = request.form['kata']
        method = request.form['method']
        language = request.form['language']

        terjemahan = translate(kata, language, method)

        # melakukan ekstraksi pada setiap file yang telah diinput
        # file harus berada pada folder "test"
        
        return render_template('index.html', terjemahan = terjemahan, language = language, kata = kata, method = method)

# halaman tentang website yang dibuat
@app.route('/about')
def about():
    return render_template('about.html')

# ketika dipanggil sebagai program utama, maka akan menjalankan server
if __name__ == '__main__' :
    app.run(debug = True)