lalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ualphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar_cipher(text, key):
    final = ''
    for letter in text:
        try:
            pos = lalphabet.index(letter)
            pos = (pos + key) % 26
            final = final + lalphabet[pos]
        except:
            try:
                pos = ualphabet.index(letter)
                pos = (pos + key) % 26
                final = final + ualphabet[pos]
            except:
                final = final + letter
    return final

def caesar_decipher(text, key):
    final = ''
    for letter in text:
        try:
            pos = lalphabet.index(letter)
            pos = (pos - key) % 26
            final = final + lalphabet[pos]
        except:
            try:
                pos = ualphabet.index(letter)
                pos = (pos - key) % 26
                final = final + ualphabet[pos]
            except:
                final = final + letter
    return final

def keyword_int(keyword):
    key = list()
    keyword = keyword.strip()
    for letter in keyword:
        try:
            pos = lalphabet.index(letter)
        except:
            try:
                pos = ualphabet.index(letter)
            except:
                print('Invalid keyword!')
                quit()
        key.append(pos)
    return key

def vigenere_cipher(text, key):
    final = ''
    n = 0
    for letter in text:
        try:
            pos = lalphabet.index(letter)
            pos = (pos + key[n]) % 26
            final = final + lalphabet[pos]
        except:
            try:
                pos = ualphabet.index(letter)
                pos = (pos + key[n]) % 26
                final = final + ualphabet[pos]
            except:
                final = final + letter
                continue
        n = (n + 1) % len(key)
    return final

def vigenere_decipher(text, key):
    final = ''
    n = 0
    for letter in text:
        try:
            pos = lalphabet.index(letter)
            pos = (pos - key[n]) % 26
            final = final + lalphabet[pos]
        except:
            try:
                pos = ualphabet.index(letter)
                pos = (pos - key[n]) % 26
                final = final + ualphabet[pos]
            except:
                final = final + letter
                continue
        n = (n + 1) % len(key)
    return final

def caesar_brute_force(text):
    for i in range(0,26):
        print(i)
        print(caesar_decipher(text, i))
        print("\n")
    return

def by_parts_inverse(text, size):
    final = ''
    lAltAlphabet = []
    uAltAlphabet = []
    index = 0
    while index < 26:
        for x in range(index + size - 1, index - 1, -1):
            lAltAlphabet.append(lalphabet[x])
            uAltAlphabet.append(ualphabet[x])
        if index == 25: break
        elif index + size >= 25: index = 25
        else: index = index + size
        if index + size > 26: size = 26 - index

    for letter in text:
        try:
            pos = lalphabet.index(letter)
            final = final + lAltAlphabet[pos]
        except:
            try:
                pos = ualphabet.index(letter)
                final = final + uAltAlphabet[pos]
            except:
                final = final + letter
    return final

def by_parts_inverse_alt(text, size):
    final = ''
    lAltAlphabet = []
    uAltAlphabet = []
    index = 0
    while index < 26:
        for x in range(index + size - 1, index - 1, -1):
            lAltAlphabet.append(lalphabet[x])
            uAltAlphabet.append(ualphabet[x])
        if index == 25: break
        elif index + size >= 25: index = 25
        else: index = index + size
        if index + size + size > 26: size = 26 - index

    for letter in text:
        try:
            pos = lalphabet.index(letter)
            final = final + lAltAlphabet[pos]
        except:
            try:
                pos = ualphabet.index(letter)
                final = final + uAltAlphabet[pos]
            except:
                final = final + letter
    return final
