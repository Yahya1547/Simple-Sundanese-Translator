def extractIndoToSunda() :
    kamus = open("../data/indoToSunda.txt", "r")
    kata = kamus.readlines()

    kamusIndoToSunda = []

    for line in kata :
        terjemahan = line.split(' = ')
        if(terjemahan[1][-1] == '\n') :
            terjemahan[1] = terjemahan[1][:-1]
            
        kamusIndoToSunda.append((terjemahan[0], terjemahan[1]))
    
    return kamusIndoToSunda

def extractSundaToIndo() :
    kamus = open("../data/sundaToIndo.txt", "r")
    kata = kamus.readlines()

    kamusSundaToIndo = []

    for line in kata :
        terjemahan = line.split(' = ')
        if(terjemahan[1][-1] == '\n') :
            terjemahan[1] = terjemahan[1][:-1]
            
        kamusSundaToIndo.append((terjemahan[0], terjemahan[1]))
    
    return kamusSundaToIndo
