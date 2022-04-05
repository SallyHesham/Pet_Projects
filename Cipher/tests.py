from cipher import (by_parts_inverse, by_parts_inverse_alt, caesar_cipher,
caesar_decipher, caesar_brute_force, vigenere_cipher, vigenere_decipher,
keyword_int)

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
txt = 'ygykq ykck\nmkrpzkq tnelik'
print(txt)
print(by_parts_inverse_alt(txt, 5))
