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

#file = open('romeo.txt').read()
#key = keyword_int('aab ')
#print(vigenere_decipher('Ad.siao .aab', key))
#txtFile = open('domain_script.txt').read()
#keyFile = open('domain_script_keys_3.txt').read()
#caesar_brute_force(txtFile)
#words = txtFile.split()
#keys = keyFile.split()
#for key, word in zip(keys, words):
    #print(caesar_decipher(word, int(key)))
key = keyword_int('peacock')
txt = 'I am the outlander. Traveler of countless worlds.'
#txt = txtFile.split()
#for word in txt[::-1]:
    #print(vigenere_decipher(word, key))
#txtFile2 = open('domain_script_reverse.txt').read()
print(txt)
print(vigenere_cipher(txt, key))
#print(vigenere_decipher(txtFile2, key))
