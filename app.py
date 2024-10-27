from flask import Flask, render_template, request
import random

app = Flask(__name__)

sehirler = ['Bursa', 'Kutahya', 'Istanbul']
konumlar = ['Is Yeri', 'Denizalti', 'Arac Tamirhanesi']
meslekler = ['Doktor', 'Muhendis', 'Hemsire']
unluler = ['Hadise', 'Mesut Sure', 'Serdar Ortac']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/oyun', methods=['POST'])
def oyun():
    kisisayisi = int(request.form.get('kisisayisi'))
    konuSecim = int(request.form.get('konuSecim'))
    spySayisi = int(request.form.get('spySayisi'))

    # Konuya göre rastgele kelime listesini seçiyoruz
    if konuSecim == 1:
        randomKelimeList = sehirler
    elif konuSecim == 2:
        randomKelimeList = konumlar
    elif konuSecim == 3:
        randomKelimeList = meslekler
    elif konuSecim == 4:
        randomKelimeList = unluler
    else:
        return "Geçersiz bir konu seçimi yapıldı.", 400

    secilenKelime = random.choice(randomKelimeList)
    oyuncuList = [(i + 1, secilenKelime) for i in range(kisisayisi)]
    spySecilen = random.choice(oyuncuList)
    oyuncuList[oyuncuList.index(spySecilen)] = (spySecilen[0], "???")

    if spySayisi == 2:
        spySecilen2 = random.choice(oyuncuList)
        while spySecilen2 == spySecilen:
            spySecilen2 = random.choice(oyuncuList)
        oyuncuList[oyuncuList.index(spySecilen2)] = (spySecilen2[0], "???")

    return render_template('result.html', oyuncuList=oyuncuList)

if __name__ == '__main__':
    app.run(debug=True)
