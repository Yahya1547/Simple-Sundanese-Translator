from extract import *
from stringmatching import *

kamusIndo = extractIndoToSunda()
kamusSunda = extractSundaToIndo()

def concat(kata, start, end) :
    # kata masih berupa list of string
    # akan menggabungkan string yang berada pada indeks start sampai end dengan tambahan spasi di antara setiap string

    sentence = ""
    for i in range(start, end + 1) :
        if i == start :
            sentence = kata[i]
        else :
            sentence = sentence + " " + kata[i]
    
    # mengembalikan string hasil penggabungan
    return sentence

def removeSymbol(kata) :
    kata_tanpa_simbol = []
    simbol = {}

    for i in range(len(kata)) :
        # Pisahkan kata dengan simbol yang "menempel" pada suatu kata

        # Sebuah simbol akan memiliki lowercase dan uppercase yang sama
        if(kata[i][-1].lower() == kata[i][-1].upper()) : 
            kata_tanpa_simbol.append(kata[i][:-1])
            simbol[i] = kata[i][-1]
        else :
            kata_tanpa_simbol.append(kata[i])
    
    return kata_tanpa_simbol, simbol

def translateKata(kosakata, language, method) :
    # kosakata ini merupakan pattern yang akan dicari pada data kamus
    # indo bernilai true apabila kosakata dalam bahasa indonesia, dan false apabila dalam bahasa sunda
    # method merupakan pilihan algoritma untuk pencocokan string
    if language == 'indo' :
        for tuplekata in kamusIndo :
            if len(tuplekata[0]) == len(kosakata) :
                if method == 'kmp' :
                    pos = kmp(tuplekata[0], kosakata)
                elif method == 'bm' :
                    pos = boyerMoore(tuplekata[0], kosakata)
                elif method == 'regex' :
                    pos = regexMatch(tuplekata[0], kosakata)
                
                if pos == 0 :
                    return (1,tuplekata[1])
    elif language == 'sunda' :
        for tuplekata in (kamusSunda) :
            if len(tuplekata[0]) == len(kosakata) :
                if method == 'kmp' :
                    pos = kmp(tuplekata[0], kosakata)
                elif method == 'bm' :
                    pos = boyerMoore(tuplekata[0], kosakata)
                elif method == 'regex' :
                    pos = regexMatch(tuplekata[0], kosakata)
                
                if pos == 0 :
                    return (1, tuplekata[1])

    # keluaran dari fungsi ini berupa tuple
    # indeks pertama dari tuple bernilai 1 apabila ditemukan kosakata dalam kamus dan 0 apabila tidak ditemukan
    # apabila indeks pertama bernilai 1, maka indeks kedua akan berisi string hasil terjemahan dari kosakata
    # apabila indeks pertama bernilai 0, maka indeks kedua akan berisi kosakata lagi tanpa diterjemahkan
    
    return (0, kosakata)




def translate(teks, language, method) : 
    kata = teks.split(' ')
    kata_tanpa_simbol, simbol = removeSymbol(kata)

    kata_terjemahan = []
    i = 0
    while i < (len(kata)) : 

        for j in range(len(kata) - 1, i-1, -1) :
            kosakata = concat(kata_tanpa_simbol, i, j)
            kosakata_terjemahan = kosakata
            terjemahan = translateKata(kosakata, language, method)
            if terjemahan[0] == 1 :
                kosakata_terjemahan = terjemahan[1]

                if j in simbol :
                    kosakata_terjemahan = kosakata_terjemahan + simbol[j]
                break
        
        kosakata_terjemahan = kosakata_terjemahan.split(' ')
        for k in range(len(kosakata_terjemahan)) :
                kata_terjemahan.append(kosakata_terjemahan[k])
        
        i = j + 1

    return concat(kata_terjemahan, 0, len(kata_terjemahan)-1)
    

print(translate("maneh kaditu? jauh? atawa kaos sangsang?", 'sunda', 'regex'))