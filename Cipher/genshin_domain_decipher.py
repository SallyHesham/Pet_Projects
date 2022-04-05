from cipher import (by_parts_inverse, by_parts_inverse_alt, caesar_cipher,
caesar_decipher, caesar_brute_force, vigenere_cipher, vigenere_decipher,
keyword_int)

text = open('domain_script.txt').read()
print("ORIGINAL:\n", text)
print("_____________________________________________________________________\n")
for i in range(1, 27):
    print(i, ":\n")

    print(by_parts_inverse_alt(text, i))
    #print("_____________________________________________________________________\n")

    print(by_parts_inverse(text, i))
    print("_____________________________________________________________________\n")
