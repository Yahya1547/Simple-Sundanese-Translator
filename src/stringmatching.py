import re

def bruteforce(teks, pattern) :
    n = len(teks)
    m = len(pattern)
    for i in range(n - m + 1) :
        j = 0
        while j < m and teks[i+j].lower() == pattern[j].lower() :
            j += 1
        if j == m :
            return i
    
    return -1


def borderFunction(pattern) :
    fail = [0 for i in range(len(pattern))]
    fail[0] = 0

    m = len(pattern)
    j = 0
    i = 1
    while i < m :
        if pattern[j].lower() == pattern[i].lower() :
            fail[i] = j + 1
            i += 1
            j += 1
        elif j > 0 :
            j = fail[j - 1]
        else :
            fail[i] = 0
            i += 1
    
    return fail


def kmp(teks, pattern):
    border = borderFunction(pattern)
    n = len(teks)
    m = len(pattern)

    i = 0
    j = 0

    while i < n :
        if pattern[j].lower() == teks[i].lower() :
            if j == m - 1 :
                return i - m + 1
            i += 1
            j += 1
        elif j > 0 :
            j = border[j - 1]
        else :
            i += 1
    
    return -1



def buildLastOccurence(teks, pattern) :
    # membentuk last occurence
    lo = {}

    # inisialisasi -1
    for char in teks.lower() :
        lo[char] = -1

    # membentuk last occurence dari pattern
    for i, char in enumerate(pattern) :
        lo[char.lower()] = i

    return lo

def boyerMoore(teks, pattern) :
    lo = buildLastOccurence(teks, pattern)

    n = len(teks)
    m = len(pattern)
    i = m - 1
    if(i > n - 1) :
        return -1 #artinya tidak ada

    j = m - 1

    while True :
        if teks[i].lower() == pattern[j].lower() : # kalau character match
            if j == 0 : # udah ketemu
                return i
            else :
                i -= 1
                j -= 1
        else : # terjadi mismatch
            lastOccur = lo[teks[i].lower()]
            i = i + m - min(j, 1 + lastOccur)
            j = m - 1
        
        if i > n - 1 :
            break
    
    return -1

def regexMatch(teks, pattern) :
    pattern_lower = pattern.lower()
    teks_lower = teks.lower()
    regex_pattern = r"(" + pattern_lower +")"
    hasil = re.findall(regex_pattern, teks_lower)

    # apabila pattern terdapat pada teks
    if len(hasil) > 0 :
        return teks_lower.find(hasil[0])
    else : # pattern tidak terdapat pada teks
        return -1
